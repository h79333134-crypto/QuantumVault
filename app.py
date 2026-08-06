from flask import Flask, render_template, request, redirect, flash, send_file
import os

from crypto.hybrid import encrypt_for_receiver, decrypt_for_receiver
from utils.key_loader import load_public_key, load_private_key

app = Flask(__name__)
app.secret_key = "quantumvault"

UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted"
DECRYPTED_FOLDER = "decrypted"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

# Temporary storage for demo (no database)
file_info = {}


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("home.html")


# ---------------- DHRUV ----------------

@app.route("/dhruv")
def dhruv():
    return render_template("dhruv.html")


# ---------------- SEND ----------------

@app.route("/send", methods=["POST"])
def send():

    uploaded_file = request.files["file"]
    receiver = request.form["receiver"]

    if uploaded_file.filename == "":
        flash("Please choose a file.")
        return redirect("/dhruv")

    # Save uploaded file
    original_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.filename
    )

    uploaded_file.save(original_path)

    # Encrypted output
    encrypted_path = os.path.join(
        ENCRYPTED_FOLDER,
        uploaded_file.filename + ".enc"
    )

    # Load receiver public key
    public_key = load_public_key(receiver)

    # Hybrid Encryption
    ciphertext, nonce = encrypt_for_receiver(
        original_path,
        encrypted_path,
        public_key
    )

    # Store metadata for demo
    file_info["latest"] = {
        "filename": uploaded_file.filename,
        "receiver": receiver,
        "encrypted_path": encrypted_path,
        "ciphertext": ciphertext,
        "nonce": nonce
    }

    flash("✅ File Encrypted & Sent Successfully!")

    return redirect("/dhruv")


# ---------------- RAHUL ----------------

@app.route("/rahul")
def rahul():

    info = file_info.get("latest")

    return render_template(
        "rahul.html",
        file=info
    )


@app.route("/rahul/decrypt")
def rahul_decrypt():

    info = file_info.get("latest")

    if not info:
        return "No file available."

    private_key = load_private_key("rahul")

    output_path = os.path.join(
        DECRYPTED_FOLDER,
        info["filename"]
    )

    decrypt_for_receiver(
        info["encrypted_path"],
        output_path,
        private_key,
        info["ciphertext"],
        info["nonce"]
    )

    return send_file(
        output_path,
        as_attachment=True
    )


# ---------------- EVE ----------------

@app.route("/eve")
def eve():

    info = file_info.get("latest")

    return render_template(
        "eve.html",
        file=info
    )


@app.route("/eve/decrypt")
def eve_decrypt():

    info = file_info.get("latest")

    if not info:
        return "No file available."

    private_key = load_private_key("eve")

    output_path = os.path.join(
        DECRYPTED_FOLDER,
        "eve_" + info["filename"]
    )

    try:

        decrypt_for_receiver(
            info["encrypted_path"],
            output_path,
            private_key,
            info["ciphertext"],
            info["nonce"]
        )

        # This should never happen
        return "<h2>Unexpected Success</h2>"

    except Exception:

        return render_template("unauthorized.html")


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)