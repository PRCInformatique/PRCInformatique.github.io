#Coding:utf-8

class salaire:
	def __init__ (self,salaire_mois):
		self._salaire_mois = salaire_mois
		self.salaire_mois = salaire_mois

	def __radd__(self,nbre_mois):
		return self.__add__(nbre_mois)

	def __add__(self,nbre_mois):
		sas = self._salaire_mois * nbre_mois
		self.salaire_mois += sas
		return self.salaire_mois

	def __sub__(self,nbre_mois):
		sals = self._salaire_mois * nbre_mois
		self.salaire_mois -= sals
		return self.salaire_mois

sal = salaire(30000)
un_an = sal + 6
moin_6_mois = -6 + sal
re = moin_6_mois
print (re)
