import tkinter
import pickle

def ouvrir_fichier(nom,donne,extension = "txt"):#ouvrir un fichier simple
	with open (f"{nom}.{extension}","a") as fic:
		fic.write(f"{donne}\n")
def lir_fichier(nom,extension = "txt"):#lir un fichier simple
	with open (f"{nom}.{extension}","r") as fic:
		return fic.read()
def ouvrir_fichier_b(nom,donne,extension = "data"):#ouvrir un fichier binaire
	with open (f"{nom}.{extension}","wb") as fic:
		sauv = pickle.Pickler(fic)
		sauv.dump(donne)
def lir_fichier_b(nom,extension = "data"):#lir un fichier binaire
	with open (f"{nom}.{extension}","rb") as fic:
		rec = pickle.Unpickler(fic)
		return rec.load() 
operateur = lambda:"+ - * / % ".split(" ")
def r_operateur(valeur1,signe,valeur2):#Fonction de calcule simple
	if signe == "+":
		return int(valeur1) + int(valeur2)
	if signe == "-":
		return int(valeur1) - int(valeur2)
	if signe == "*":
		return int(valeur1) * int(valeur2)
	if signe == "/":
		return int(valeur1) / int(valeur2)
	if signe == "%":
		return int(valeur1) % int(valeur2)

def ponctuation():
	return ". , ; : ! ?".split(" ")
def calcule (*args):
	if len(args) == 1:
		args = args[0].split(" ")
	if "(" not in args:
		a = 0
		for nbre in args:
			if nbre in operateur() and a<2:
				resultat = r_operateur(args[a-1],args[a],args[a+1])
			if a > 2:
				if nbre in operateur():
					valeur1 = resultat
					resultat = r_operateur(valeur1,args[a],args[a+1])
			a+=1
	return resultat

def conver_M(fonction,dic):
	a = 0
	for k in dic.keys():
		a += fonction(dic[k],k)
	return a

