from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)


# Fonction pour lire un fichier texte et renvoyer une liste de lignes
def lire_fichier_texte(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


# Charger les extraits de phrases depuis les fichiers texte
debut_phrases = lire_fichier_texte('début.txt')
milieu_phrases = lire_fichier_texte('milieu.txt')
milieu2_phrases = lire_fichier_texte('milieu2.txt')
fin_phrases = lire_fichier_texte('fin.txt')


# Route pour obtenir un horoscope aléatoire pour un signe donné
@app.route('/horoscope/<signe>', methods=['GET'])
def generer_horoscope(signe):
    if signe not in ['bélier', 'taureau', 'gemeaux', 'cancer', 'lion', 'vierge', 'balance', 'scorpion', 'sagittaire',
                     'capricorne', 'verseau', 'poissons']:
        return jsonify({"erreur": "Signe du zodiaque invalide"}), 400

    horoscope = {
        "signe": signe,
        "horoscope": f"{random.choice(debut_phrases)} {signe.capitalize()} {random.choice(milieu_phrases)}{random.choice(milieu2_phrases)} {random.choice(fin_phrases)}"
    }

    return jsonify(horoscope)

@app.route('/')
def accueil():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)