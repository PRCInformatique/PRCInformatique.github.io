#coding:utf-8
from fonction import *
"""
Classe de trie d'information.
Prend en paramètre un dictionnaire (optionnel)
qui à en clé les pays et en valeur les sources vérifiées

Les méthodes définies sont:

-------- annalyse_info(). Son appel permet de faire l'annalyse de l'information.
C'est une méthode d'instance qui ne prend rien en paramètre
Mais demande des informations bien précis sur l'information a annalysé

-------- voir_donne(). Son appel permet de voir les données qui ont été attesté vrai.
Seul les administrateur sont autorisés a utilisé cette fonction.
C'est une méthode d'instance qui ne prend rien mais demande des informations bien précis

-------- dic. son appel permet d'accéder aux source de vérification inséré. Seul les 
administrateurs et les visiteurs agréés c'est_à_dire ceux qui ont passé un dictionnaire 
de source en paramètre de créations de l'objet.
"""

class Smart:
	#classe smart pour le trie des informations
	#Avec une vérifiction administrative pour l'acccès des archives.

	def __init__ (self,dic = "none"):
		#prend en paramètre un dictionnaire optionel.
		#Vérification d'identité:
		self.adminis = False
		self.visiteur_agre = False
		nom = input ("Nom: ")
		mot_de_pass = input ("Mot de passe: ")
		if nom == administrateur()["nom"] and mot_de_pass == administrateur()["mot_de_pass"]:#Vérifier si il s'agit de l'administrateur par une fonction
			self.adminis = True
		if type(dic) != dict and dic != "none": #Vérification du type de donnée entré.
			print (f"Cette classe attend un dictionnaire comme paramètre. Pas un {type(dic)}.")
			return
		if type (dic) == dict: #prendre en compte les sources entrés comme fiable
			self._dic = dic
			source_sauvegarde(self._dic)
			self.visiteur_agre = True 
		elif dic == "none": #prendre en compte les sources déjà utilisées
			print ("Vous voulez accéder au sources déjà approuver..")
			self._dic = source()

	def annalyse_info(self):#Fonction d'annalyse d'information
		info = input("Votre information: ")
		source = input ("Votre source: ")
		pays = input ("Pays: ")
		dic = {
		"info":f"{info}",
		"source":f"{source}",
		"pays":f"{pays}"
		}
		recherche = search(self._dic,pays,source)
		if recherche == True: #Enrégistrement si l'information est vrai
			print ("Votre information est Vrai: ")
			date = input ("Entrer la date du jour si vous voulez enrégistré votre info: ")
			if len (date) > 0:
				dic["date"] = date
				sauvergarde(dic) #Enrégistrement officiel
			else:
				print("Votre information n'a pas été enrégistré")
				non_sauvegarder(dic) #Enrégistrement secret

	def voir_donne(self):#Méthode qui permet de voir les données
		if self.adminis == False:
			mot_de_pass = input("Accès non autorisé. Veillez confirmé \nvotre mot de passe si vous êtes l'administrateur: ")
			if mot_de_pass == administrateur()["mot_de_pass"]:
				self.adminis = True
		elif self.adminis == True:#vérification de qui veux accéder a cette partie du code
			print ("Vous avez accès au informations...")
			type_d_information = input("Quel sauvergarde voulez vous voir? officiel ou secret?: ")
			while type_d_information != officiel or type_d_information != secret:#Vérification de la saisie
				print("Vous Vous êtes surement trompé. Veillez respecter l'orthographe SVP")
				type_d_information = input("Quel sauvergarde voulez vous voir? officiel ou secret?: ")
			if type_d_information == 'secret':
				return info_secret()
			elif type_d_information == 'officiel':
				return info_officiel()

	def _get_dic(self,passe = ''):
		if self.visiteur_agre == True:#Accès source
			return self._dic
		elif passe != administrateur()["mot_de_pass"]:
			if self.adminis == False:
				mot_de_pass = input("Veillez confirmé votre mot de passe: ")
				if mot_de_pass == administrateur()["mot_de_pass"]:
					self.adminis == True
					print("Accès autorisé")
					return self._dic
				else:
					print ("Seul les Aministrateurs ont accès a cette fonctionalité")

	def _set_dic(self,nouveau_valeur,passe = ''):
		if type(nouveau_valeur) != dict: #Vérification du type de donnée entré.
				print (f"Vous dévez entré un dictionnaire comme Valeur. Pas un {type(nouveau_valeur)}.")
				return
		if self.visiteur_agre == True:#Accès source individuel
				self._dic = nouveau_valeur
		elif passe != administrateur()["mot_de_pass"]:
			if self.adminis == False:
				mot_de_pass = input("Veillez confirmé votre mot de passe: ")
				if mot_de_pass == administrateur()["mot_de_pass"]:
					self.adminis == True
					self._dic = nouveau_valeur
					print("Accès autorisé")
				else:
					print ("Seul les Aministrateurs ont accès a cette fonctionalité")

	dic = property(_get_dic,_set_dic)