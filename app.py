
from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

def generate_natural_passphrase():
    sujets = [
        "Je", "Tu", "Il", "Elle", "Nous", "Vous", "Ils", "Elles",
        "Mon frère", "Ma sœur", "Le chat", "Le chien", "Le professeur", "Un ami",
        "Le voisin", "Ma mère", "Le médecin", "Le policier", "Le facteur"
    ]

    verbes = [
        "mange", "lit", "joue", "court", "dort", "regarde", "prend", "trouve", "cherche", "porte",
        "ouvre", "ferme", "écrit", "aime", "entend", "voit", "explique", "apprend", "utilise", "prépare",
        "répare", "construit", "détruit", "observe", "dessine", "signe", "nettoie", "analyse", "commente", "traduit"
    ]

    complements = [
        "une pomme", "un livre", "la porte", "le ballon", "une chaise", "un vélo", "le pain",
        "dans la rue", "au parc", "à l’école", "dans la maison", "sur le bureau", "avec son ami",
        "dans le jardin", "sous la table", "près de l’arbre", "à la bibliothèque", "à la cuisine",
        "dans le salon", "au garage", "dans la forêt", "sur le toit", "sur le canapé", "dans le grenier",
        "dans la voiture", "au cinéma", "au marché", "sur la plage", "dans le train", "dans l’avion"
    ]

    sujet = random.choice(sujets)
    verbe = random.choice(verbes)
    complement = random.choice(complements)

    return f"{sujet} {verbe} {complement}"

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        password = generate_natural_passphrase()
    return render_template("index.html", password=password)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
