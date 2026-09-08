from flask import Flask, render_template, request, send_file, after_this_request
from werkzeug.utils import secure_filename
import os, random, string

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

otp_store = {}  # otp -> filepath

def generate_otp():
    return "".join(random.choices(string.digits, k=6))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file.filename != "":
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            otp = generate_otp()
            otp_store[otp] = filepath

            return render_template("otp_result.html", otp=otp)

    return render_template("upload.html")

@app.route("/retrieve", methods=["GET", "POST"])
def retrieve():
    error = None
    if request.method == "POST":
        otp = request.form.get("otp")
        filepath = otp_store.get(otp)

        if filepath and os.path.exists(filepath):
            response = send_file(filepath, as_attachment=True)
            del otp_store[otp]
            try:
                os.remove(filepath)
            except OSError:
                pass
            return response
        else:
            error = "Invalid or expired OTP. Please try again."

    return render_template("retrieve.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)