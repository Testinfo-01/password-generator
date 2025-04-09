from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

# Français
sujets_fr = ["Je", "Tu", "Il", "Elle", "Nous", "Vous", "Ils", "Elles"]
verbes_fr = ["mange", "lit", "joue", "court", "dort", "regarde", "prend", "trouve", "cherche", "ouvre"]
complements_fr = ["une pomme", "un livre", "le ballon", "dans la rue", "au parc", "à l’école", "dans le jardin"]

# English
sujets_en = ["I", "You", "He", "She", "We", "They"]
verbes_en = ["eat", "read", "play", "run", "sleep", "watch", "take", "find", "look for", "open"]
complements_en = ["an apple", "a book", "the ball", "in the street", "at the park", "at school", "in the garden"]

def generate_phrase(lang="fr"):
    if lang == "en":
        sujet = random.choice(sujets_en)
        verbe = random.choice(verbes_en)
        complement = random.choice(complements_en)
        return f"{sujet} {verbe} {complement}"
    else:
        sujet = random.choice(sujets_fr)
        verbe = random.choice(verbes_fr)
        complement = random.choice(complements_fr)
        return f"{sujet} {verbe} {complement}"

def add_security_elements(phrase, add_numbers=False, add_symbols=False, position="end"):
    numbers = "1234567890"
    symbols = "!@#$%^&*"
    prefix = ""
    suffix = ""

    if add_numbers:
        n = random.choice(numbers)
        prefix += n if position == "start" else ""
        suffix += n if position == "end" else ""
    if add_symbols:
        s = random.choice(symbols)
        prefix += s if position == "start" else ""
        suffix += s if position == "end" else ""

    return f"{prefix}{phrase}{suffix}"

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        lang = request.form.get("langue", "fr")
        add_numbers = "add_numbers" in request.form
        add_symbols = "add_symbols" in request.form
        position = request.form.get("position", "end")

        phrase = generate_phrase(lang)
        password = add_security_elements(phrase, add_numbers, add_symbols, position)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
