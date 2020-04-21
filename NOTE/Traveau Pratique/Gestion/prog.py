#Coding:utf-8
import classe


def conect():
	conx_insc = input ("connexion ou inscription: ")
	if "conne" in conx_insc:
		pseudo = input ("pseudo: ")
		mot_de_passe = input ("mot de passe: ")
		pseudo = classe.Connexion().identifier(pseudo,mot_de_passe)
	else :
		nom = input ("votre nom: ")
		prenom = input ("votre prénom: ")
		pseudo = input ("Choisie un pseudo unique a vous: ")
		mot_de_passe = input("Votre mot de passe: ")
		print (classe.Connexion().enregistrement(nom,prenom,pseudo,mot_de_passe))
	return pseudo
entr = {
	"aa":8566,
	"ap":4856,
	"az":4566
}
sort = {}
mobile = classe.Gestion("20-4-20","mobile",conect())
print ("entrer")
print (mobile.entre(entr))
print ("sortie")
print (mobile.sorti(sort))
print ("reste")
print (mobile.reste())
print ("espace de travail")
print (mobile.espace_de_travail())
