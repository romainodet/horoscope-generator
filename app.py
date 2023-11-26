from flask import *
from horoscope import *

app = Flask(__name__)


# defintion de la page d'accueil
@app.route('/')
@app.route('/index.html')# / is the URL
def index():
    liste = horoscope()
    print(liste)
    belier = liste[0]
    taureau = liste[1]
    gemeaux = liste[2]
    cancer = liste[3]
    lion = liste[4]
    vierge = liste[5]
    balance = liste[6]
    scorpion = liste[7]
    sagittaire = liste[8]
    capricorne = liste[9]
    verseau = liste[10]
    poissons = liste[11]

    return render_template('index.html', belier=belier,taureau=taureau,gemeaux=gemeaux,cancer=cancer,lion=lion,vierge=vierge,balance=balance,scorpion=scorpion,sagittaire=sagittaire,capricorne=capricorne,verseau=verseau,poissons=poissons)  # afficher la page index html


if __name__ == '__main__':
    app.run()
