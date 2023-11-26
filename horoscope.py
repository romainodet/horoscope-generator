def horoscope():
    import random
    
    signes_file = open("signes.txt", "r")
    signes_data = signes_file.read()
    signes = signes_data.split("\n")
    signes_file.close()
    
    debut_file = open("debut.txt", "r")
    debut_data = debut_file.read()
    debut = debut_data.split("\n")
    debut_file.close()
    
    milieu_file = open("milieu.txt", "r")
    milieu_data = milieu_file.read()
    milieu = milieu_data.split("\n")
    milieu_file.close()
    
    milieu2_file = open("milieu2.txt", "r")
    milieu2_data = milieu2_file.read()
    milieu2 = milieu2_data.split("\n")
    milieu2_file.close()
    
    fin_file = open("fin.txt", "r")
    fin_data = fin_file.read()
    fin = fin_data.split("\n")
    fin_file.close()

    parcours_liste = 0
    prenom = 1
    list_return = []

    while len(signes) > parcours_liste:
        debut_phrase = ""
        milieu_phrase = ""
        fin_phrase = ""
        phrase = ""
        signe_act = signes[parcours_liste]
        debut_phrase = random.choice(debut)
        milieu_phrase = random.choice(milieu)
        milieu_phrase_2 = random.choice(milieu2)
        fin_phrase = random.choice(fin)

        if prenom == 1:
            phrase = debut_phrase + " " + signe_act + ", " + milieu_phrase + "" +  milieu_phrase_2 + " " + fin_phrase
        elif prenom == 2:
            phrase = debut_phrase + ", " + milieu_phrase + " " + signe_act + "" + milieu_phrase_2 + " " + fin_phrase
        elif prenom == 3:
            phrase = debut_phrase + ", " + milieu_phrase + "" + milieu_phrase_2 + " " + signe_act + " " + fin_phrase
        list_return.append(signe_act + " : " + phrase + ".")  # add actual sign before the sent

        parcours_liste += 1
        prenom += 1
        if prenom > 3:
            prenom = 1
    return list_return