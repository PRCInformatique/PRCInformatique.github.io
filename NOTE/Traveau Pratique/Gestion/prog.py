#Coding:utf-8
import francais as Fr 
import defi 
#classe Ampèremetre
class Amperemetre:
	def conversion_A(valeur, unite):
		dic = {
		"kA": valeur*(10**3),
		"mA": valeur*(10**-3),
		"miA": valeur*(10**-6),
		"A" : valeur
		}
		return dic[unite]

	Am = staticmethod(conversion_A)

	def __init__(self,aiguille = False,**args):
		self.A = Fr.conver_M(fonction = Amperemetre.conversion_A, dic = args)
		self.aiguille = aiguille
		self.def_Calibre = defi.Calibre

	def definition(cls):
		return defi.Amperemetre
	definition = classmethod(definition)

	def Definition(self,):
		if self.aiguille == True:
			return defi.Amperemetre_aiguille
		else:
			return Amperemetre.definition

	def Intensite(self,**par):
		if self.aiguille == True:
			Ic = par['Ic']
			n = par['n']
			N = par['N']
			return defi.Calcule_intensité(Ic,n,N)
		else:
			return par["intensite"]

	def Calibre_Apareil(self,calibre_max,intensite_max):
		intens = 0
		while intens < intensite_max:
			calibr = int(input('Calibre: '))
			intens = int(input("intensite: "))
		return calibr

	def __add__(self,valeur):
		In = self.Intensite(**par)
		return In + valeur


a = Amperemetre(A = 35)
print(Amperemetre.conversion_A(25,"kA"))

class Voltmetre:
	def __init__(**args):

		pass

#Classe de mesures de l'intensité, de la tension et de la resistance: LOI D'OHM
#class InTeRe:
