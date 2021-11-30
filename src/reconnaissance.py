from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image,liste_modeles,S):
    resultat = 0
    similitude = 0
    similitude_max = 0
    image2 = image.localisation()
    for i in range (len(liste_modeles)):
        H = liste_modeles[i].H
        W = liste_modeles[i].W
        image2 = image2.resize(H, W)
        similitude = image2.similitude(liste_modeles[i])
        if similitude >= similitude_max :
            similitude_max = similitude
            resultat = i
    return resultat

