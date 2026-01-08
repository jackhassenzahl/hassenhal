#!/var/www/html/hassenhal/card/.venv/bin/python

import sys
import qrcode
import numpy as np
import subprocess
from pathlib import Path

# ---------------- SETTINGS ----------------
TEXT = sys.argv[1]
JOB = sys.argv[2]  # job ID passed from worker
CARD_FILE = "template.scad"      # existing SCAD file
OUTPUT_SCAD = f"jobs/done/{JOB}.scad"
OUTPUT_STL = f"jobs/done/{JOB}.stl"
MODULE = 1.0
HEIGHT = 2.0
GAP = -0.01
BORDER = 2

# ---------------- GENERATE SCAD ----------------
with open(CARD_FILE, "r") as f:
    scad_lines = f.readlines()

qr = qrcode.QRCode(border=BORDER)
qr.add_data(TEXT)
qr.make(fit=True)
matrix = np.array(qr.get_matrix(), dtype=int)
h, w = matrix.shape

qr_lines = ["module qr_code() {", "    union() {"]
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
                f"        translate([{xpos + GAP/2}, {ypos + GAP/2}, 0]) cube([{width}, {MODULE - GAP}, {HEIGHT}]);"
            )
        else:
            x += 1
qr_lines.append("    }")
qr_lines.append("}")

# Combine template + QR
output_lines = scad_lines + ["\n"] + qr_lines
with open(OUTPUT_SCAD, "w") as f:
    f.writelines(output_lines)

# ---------------- GENERATE STL ----------------
openscad_exe = "/usr/bin/openscad"
cmd = [openscad_exe, "-o", str(OUTPUT_STL), str(OUTPUT_SCAD)]
result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode != 0:
    print("OpenSCAD error:")
    print(result.stderr)
else:
    print("STL exported:", OUTPUT_STL)
