from flask import Flask, render_template, request
import random
import string
import os

app = Flask(__name__)

def generate_password(length=12, use_digits=True, use_upper=True, use_special=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    
    if not chars:
        return ""
    
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        use_digits = "digits" in request.form
        use_upper = "upper" in request.form
        use_special = "special" in request.form
        password = generate_password(length, use_digits, use_upper, use_special)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
