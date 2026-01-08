#!/var/www/html/hassenhal/card/.venv/bin/python

import sys
import qrcode
import numpy as np
import subprocess
from pathlib import Path

# ---------------- SETTINGS ----------------
TEXT = sys.argv[1]
CARD_FILE = "template.scad"      # existing SCAD file
OUTPUT_FILE = "qr_code.scad"
MODULE = 1.0
HEIGHT = 2.0
GAP = -0.01
BORDER = 2

def scadfile():
    # ---------------- READ EXISTING SCAD ----------------
    with open(CARD_FILE, "r") as f:
        scad_lines = f.readlines()

    # ---------------- GENERATE QR MATRIX ----------------
    qr = qrcode.QRCode(border=BORDER)
    qr.add_data(TEXT)
    qr.make(fit=True)
    matrix = np.array(qr.get_matrix(), dtype=int)
    h, w = matrix.shape

    # ---------------- GENERATE qr_code MODULE ----------------
    qr_lines = []
    qr_lines.append("module qr_code() {")
    qr_lines.append("    union() {")
    for y in range(h):
        x = 0
        while x < w:
            if matrix[y, x]:
                # merge horizontal runs
                start_x = x
                while x < w and matrix[y, x]:
                    x += 1
                end_x = x
                xpos = start_x * MODULE
                ypos = (h - y - 1) * MODULE  # invert Y
                width = (end_x - start_x) * MODULE - GAP
                qr_lines.append(
                    f"        translate([{xpos + GAP/2}, {ypos + GAP/2}, 0]) cube([{width}, {MODULE - GAP}, {HEIGHT}]);"
                )
            else:
                x += 1
    qr_lines.append("    }")  # end union
    qr_lines.append("}")      # end module
    qr_lines.append("")       # newline for clarity

    scad_lines = [line.replace("qr_modules = 29", f"qr_modules = {x}") for line in scad_lines]

    # ---------------- COMBINE ----------------
    output_lines = scad_lines + ["\n"] + qr_lines

    with open(OUTPUT_FILE, "w") as f:
        f.writelines(output_lines)

    print(f"Saved updated SCAD file: {OUTPUT_FILE}")

def stlfile():
    openscad_exe = "/usr/bin/openscad"

    scad_file = Path("qr_code.scad")
    stl_file = Path("qr_card.stl")

    cmd = [
        openscad_exe,
        "-o", str(stl_file),
        str(scad_file)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("OpenSCAD error:")
        print(result.stderr)
    else:
        print("STL exported:", stl_file)
    return

def main():
    scadfile()
    stlfile()

main()