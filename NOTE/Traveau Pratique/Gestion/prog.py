#Coding:utf-8
#définire une classe de gestion
import pickle
class Gestion:

	def lir_b(nom):
		with open(f"{nom}",'rb') as fic:
			re = pickle.Unpickler(fic)
			rec = re.load()
		return rec
	lir_b = staticmethod(lir_b)

	def ouvrir_b(nom,donne):
		with open(f"{nom}","wb") as fic:
			sau = pickle.Pickler(fic)
			sau.dump(donne)
	ouvrir_b = staticmethod(ouvrir_b)

	def sauvegarde(nom,pseudo,mot_passe):
		ancien = lir_b(f"{nom}")
		while pseudo in ancien.keys():
			print ("Votre pseudo existe déja.")
			pseudo = input("Entrer à nouveau un autre nom d'utilisateur: ")
		ancien[pseudo] = mot_passe
	sauvegarde = staticmethod(sauvegarde)

	def inscription():
		pseudo = input ("Choisie un nom d'utilisateur: ")
		mot_passe = input ("Choisie un mot de passe: ")
		sauvegarde(pseudo,mot_passe)
	inscription = staticmethod(inscription)

	def connexion():
		inn = input("ancien ou nouveau compte? ")
		if "an" in inn:
			inscription()
			print ("connectez-vous a présent")

		dic = lir_b("dic_connexion")
		nom = input("Votre nom d'utilisateur: ")
		while nom not in dic.keys():
			print("Votre pseudo est invalide.")
			nom = input("Votre nom d'utilisateur SVP: ")
		mpasse = input("Votre mot de passe: ")
		while mpasse != dic[nom]:
			print ("Votre mot de passe est erroné")
			mpasse = input("Votre mot de passe SVP: ")
		return nom
	connexion = staticmethod(connexion)

	def __init__(self,objet):
		self.objet = objet
		self.pseudo = connexion()



#définire une classe qui permet de mettre en forme un texte en fesant un tri. Les chaines
#caractère a part et les listes a part, les tuple a part et les dictionnaires a part.
#La classe prend en paramètre une chaine de caractère et fait le tri

import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))

launched = True

while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False

