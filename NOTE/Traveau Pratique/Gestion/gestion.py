#Coding:utf-8

class Gestion:#Classe de gestion
	def __init__ (self,date,nom_objet):
		self.date = date
		self.nom_objet = nom_objet
		self.nom = ''
		self.mot_de_passe = ''
		self.pseudo = connexion.Connexion.identifier(self.nom,self.mot_de_passe)

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
		enre_oj_espace (self.pseudo,self.date,dic)
		G_dic = tri_dans_dic(self.pseudo)
		return G_dic
#*****************************************************************************************
