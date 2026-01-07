from flask import Flask, render_template, request, send_file
from qr_generator import generate_qr_stl
from pathlib import Path
import uuid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["qrtext"]
        out_file = Path("output") / f"{uuid.uuid4()}.stl"
        out_file.parent.mkdir(exist_ok=True)

        generate_qr_stl(text, out_file)

        return send_file(out_file, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
