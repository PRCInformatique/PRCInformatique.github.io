#Coding:utf-8
from fonction import *
#fichier des classes
#_____________________________ Classe de Gestion _________________________________________
class Gestion:#Classe de gestion
	def __init__ (self,date,nom_objet,pseudo):
		self.date = date
		self.nom_objet = nom_objet
		enre_objet(pseudo,nom_objet)
		self.pseudo = pseudo

	def entre (self,dic):# Retourne le grand dictionnaire et la grande listes des entrées
		donne = {
		"dic":dic,
		"date":self.date,
		"flux":'entrer'
		}
		calcule = receuil(self.nom_objet,**donne)
		self.entrer_total = calcule[-1][-1][-1] #somme des entrées
		return calcule

	def sorti (self,dic): #Retourne le grand dictionnaire et la grande listes des sorties
		donne = {
		"dic":dic,
		"date":self.date,
		"flux":'sortie'
		}
		calcule = receuil(self.nom_objet,**donne)
		self.sortie_total = calcule[-1][-1][-1] #somme des sorties
		return calcule

	def reste (self): #Retoure le reste
		self.reste_total = self.entrer_total - self.sortie_total 
		return self.reste_total

	def historique_dic(self,flux):
		return histo_dic(self.nom_objet,flux)

	def historique_lis(self,flux):
		return histo_lis(self.nom_objet,flux)

	def recherche_point (self,date = ""):
		return point(self.nom_objet,date = date)

	def espace_de_travail(self):# méthode doit être appeler automatiquement que l'on valide une entrée ou une sortie 
	# utiliser pour créer l'espace de travail.
		dic = {
		self.nom_objet : ({"entrés": self.entrer_total,"sortis": self.sortie_total,"reste": self.reste_total})
		}
		print (dic)
		enre_oj_espace (self.pseudo,self.date,dic)
		G_dic = tri_dans_dic(self.pseudo)
		return G_dic
#*****************************************************************************************

#_____________________________ Classe de Connexion _______________________________________
class Connexion:#Classe pour la sécurité d'accès
	def __init__ (self):
		self.identifiant = lir_identifiant()
		self.acces = False
	def identifier (self,pseudo,mot_de_passe): #Méthode d'identification
		pseudo.lower()
		mot_de_passe.lower()
		nom_utilisateur = verifie(pseudo,self.identifiant.keys())
		if nom_utilisateur == True:
			mo_passe = verifie_egal(mot_de_passe,self.identifiant[pseudo])
			if mo_passe == True:
				self.acces == True
				print (f"Vous vous êtes connecté en tend que {pseudo}")
				return pseudo
			else:
				print( "Mot de passe erronné")
		if nom_utilisateur == False:
			print( "Pseudo non Valide. Veillez revoir vos informations")

	def enregistrement (self,nom,prenom,pseudo,mot_de_passe): #Méthode d'enrégistrement
		pseudo.lower()
		mot_de_passe.lower()
		if len(self.identifiant)> 1:
			if verifie (pseudo,self.identifiant.keys()) == True:
				print ("Veillez Choisir un autre pseudo. Ce pseudo existe deja")
			else:
				dic_connexion = lir_fic_identifiant()
				dic_connexion[pseudo] = (nom,prenom,mot_de_passe)
				enre_fic_identifiant(dic_connexion)
				enr_identifiant(pseudo,mot_de_passe)
				return 'Vos informations ont été très bien Enrégistrées\nVeillez vous connecter à présent'
		elif len(self.identifiant) <= 1:
			dic_connexion = {}
			dic_connexion[pseudo] = (nom,prenom,mot_de_passe)
			enre_fic_identifiant(dic_connexion)
			enr_identifiant(pseudo,mot_de_passe)
			return 'Vos informations ont été très bien Enrégistrées\nVeillez vous connecter à présent'
#*****************************************************************************************

#_____________________________ Classe d'Espace de Tarvail ________________________________
"""class EspaceDeTravail:#Classe qui permet d'ouvrir une espace de travail selon l'ancienne activité
	def __init__(self,pseudo,mot_de_passe,les_objets):
		self.pseudo = Connexion().identifier(pseudo,mot_de_passe)
		self.les_objets = les_objets
	#dic prend en clé les différends objets à gérer dans notre programme de gestion
	def nouveau (self):  
		ouvrir_espace_vide(self.pseudo,self.les_objets) #Cette méthode doit initialiser un tableau vide contenant les objets à gérer
		return lir_espace_(pseudo)

	def ancien (self):
		return lir_espace(self.pseudo) #Cette méthode consiste à retourner l'ancienne Espace de tavail de de l'utilisateur.

	def mise_a_jour (self,dic): #dic est le résultat de la méthode espacedetravail de la classe gestion
		enre_espace(self.pseudo,dic) # Cette méthode permet de faire la mise à jour du travail de l'utilisateur.


"""