import qrcode
import numpy as np
import subprocess
from pathlib import Path

CARD_FILE = "template.scad"
MODULE = 1.0
HEIGHT = 2.0
GAP = -0.01
BORDER = 2
OPENSCAD = "/usr/bin/openscad"

def generate_qr_stl(text, out_stl: Path):
    scad_file = out_stl.with_suffix(".scad")

    with open(CARD_FILE) as f:
        scad_lines = f.readlines()

    qr = qrcode.QRCode(border=BORDER)
    qr.add_data(text)
    qr.make(fit=True)
    matrix = np.array(qr.get_matrix(), dtype=int)
    h, w = matrix.shape

    qr_lines = ["module qr_code() {", "  union() {"]
    for y in range(h):
        x = 0
        while x < w:
            if matrix[y, x]:
                start_x = x
                while x < w and matrix[y, x]:
                    x += 1
                end_x = x
                xpos = start_x * MODULE
                ypos = (h - y - 1) * MODULE
                width = (end_x - start_x) * MODULE - GAP
                qr_lines.append(
                    f"    translate([{xpos + GAP/2}, {ypos + GAP/2}, 0]) "
                    f"cube([{width}, {MODULE - GAP}, {HEIGHT}]);"
                )
            else:
                x += 1
    qr_lines += ["  }", "}", ""]

    out_lines = scad_lines + ["\n"] + qr_lines
    scad_file.write_text("".join(out_lines))

    subprocess.run([OPENSCAD, "-o", str(out_stl), str(scad_file)], check=True)
