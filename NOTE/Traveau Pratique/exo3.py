#Coding: utf-8
import tkinter
import pickle
def lir_b(nom):
	with open(f"{nom}","rb") as fic:
		en = pickle.Unpickler(fic)
		en = en.load()
	return en
def ouvrir_b(nom,donne):
	with open(f"{nom}",'wb') as fic:
		ef = pickle.Pickler(fic)
		ef.dump(donne)
def lis(liste):
	ll = []
	for i in liste:
		ll.append(i)
	return ll
def trouver_dans(liste1,liste2):
	ret = []
	for i in liste2:
		if i in liste1:
			ret.append(i)
		else:
			ret.append("*")

	return ret
# programme de jeu choix de mot

#fonction du jeu
def mot_harard():#Retourne un mot au hazard
	liste = "papa maman pipo pipi jesus dieu amour fidele victoire david paul jean diane kokou"
	liste = liste.split()
	import random
	hazar = random.randrange(len(liste))
	return liste[hazar]

def en_score(nom,Score):
	ouvrir_b(f"{nom}Score",Score)

def fic_score(nom):
	try:
		lir_b(f"{nom}Score")
	except:
		ouvrir_b(f"{nom}Score",0)
	return lir_b(f"{nom}Score")

def lettre(ltr,score,sc,lettre_trouver):
	LT = lis(lettre_trouver)
	mot = mot_harard()
	if ltr in mot:
		LT.append(ltr)
		LT = trouver_dans(LT,mot)
		if LT == mot:
			score += sc
			return score, sc, "END"
		else :
			return LT, sc, 'CON'
	elif ltr not in mot:
		if sc == 0:
			return LT, sc, "END"
		sc-=1
		return LT, sc, "CON"




