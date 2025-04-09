from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

# Phrases complètes en français
phrases_fr = [
    "Je mange une pomme",
    "Tu lis un livre",
    "Il joue avec le ballon",
    "Elle court dans la rue",
    "Nous dormons au parc",
    "Vous regardez un film",
    "Ils prennent un café",
    "Elles trouvent une solution",
    "Je cherche mon stylo",
    "Tu ouvres la fenêtre",
    "Il ferme la porte",
    "Elle lit une lettre",
    "Nous écrivons un message",
    "Vous entendez un bruit",
    "Ils voient une voiture",
    "Elles chantent une chanson"
]

# Phrases complètes en anglais
phrases_en = [
    "I eat an apple",
    "You read a book",
    "He plays with the ball",
    "She runs in the street",
    "We sleep at the park",
    "They watch a movie",
    "I take the train",
    "You find your keys",
    "He opens the door",
    "She closes the window",
    "We write a message",
    "They hear a sound",
    "I see a bird",
    "You drive a car",
    "He drinks coffee",
    "She sings a song"
]

def generate_phrase(lang="fr"):
    if lang == "en":
        return random.choice(phrases_en)
    else:
        return random.choice(phrases_fr)

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
    app.run(host="0.0.0.0", port=5001)


