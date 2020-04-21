#coding: utf-8
import donnees as Dn 

def ouvrir_fichier_b(nom,donne):
	import pickle
	with open(f'{nom}','wb') as fic:
		sau = pickle.Pickler(fic)
		sau.dump(donne)#ouverture de fichier binaire

def lir_fichier_b(nom):
	import pickle
	with open(f"{nom}",'rb') as fic:
		rec = pickle.Unpickler(fic)
		ret = rec.load()
	return(ret)#lecture de fichier binairaire

def sauvegarde (**paramètre):
	donne = lir_fichier_b("officiel")
	cle = (date,source)
	donnee = [(pays,info)]
	if cle in donne.keys():
		donne[cle].extend(donnee)
	else:
		donne[cle] = donnee
	ouvrir_fichier_b("officiel",donne)#Méthode de sauvegarde officielle

def source_sauvegarde(**paramètre):
	donne = lir_fichier_b("source")
	cle = (pays)
	donnee = [source]
	if cle in donne.keys():
		donne[cle].extend(donnee)
	else:
		donne[cle] = donnee
	ouvrir_fichier_b("source",donne)#Méthode se sauvegarde des sources

def non_sauvegarder(**paramètre):
	donne = lir_fichier_b("secret")
	cle = source
	donnee = [(pays,info)]
	if cle in donne.keys():
		donne[cle].extend(donnee)
	else:
		donne[cle] = donnee
	ouvrir_fichier_b("secret",donne)#Méthode de sauvegarde secret

def administrateur():
	nom = 'David'
	mot_de_passe = '32843'
	dic = {
	"nom":f"{nom}",
	"mot_de_pass":f"{mot_de_passe}"
	}
	return dic#définie les informations de l'administrateur

def info_secret():#Retourne les informations sécrètement enrégistrées
	return lir_fichier_b("secret")

def info_officiel(): #Retourne les informations officiellement enrégistrées
	return lir_fichier_b("officiel")

def source():# return la liste des sources
	return lir_fichier_b("source")

def search(sources,pays,source):
	for Pays in sources.keys():
		if pays == Pays:
			return [True for sou in sources[pays] if sou == source] #algorithme d'Annalyse

def mot_hazart():
	from random import randrange
	liste = Dn.liste_des_mots
	return liste[randrange(len(liste))]
#génère le mot à deviner

def mot_avec_lettre(score,mot_au_hazart):
	nbre_chance = Dn.nbre_chance
	mot_trouver = list()
	mot_trouver_ = ""
	while nbre_chance > Dn.fin_jeu and mot_trouver_ != mot_au_hazart:
		#Boucle du jeu
		print("Si vous entrer un chiffre, la partie sera terminé.")
		lettre_entrer = input("Veillez deviner une lettre: ")
		try :#vérifier si le joueur a bien entrer une lettre alphabétique
			int(lettre_entrer)
		except:
			pass
		else:
			print ("Vous avez entrer un chiffre au lieu d'une lettre. Jeu Terminé")
			return

		while len (lettre_entrer) != Dn.nbre_lettre:#Boucle de vérification: Si le joueur a bien entrer une lettre
			nbre_chance -= Dn.diminution_de_chance
			if len (lettre_entrer) > Dn.nbre_lettre:#Si le joueur a entré deux lettres
				if nbre_chance == Dn.fin_jeu:
					print (f"Jeu terminé. Vous n'avez pas pu deviner le mot.\nLe mot à deviner était '{mot_au_hazart}' ")
				elif nbre_chance > Dn.fin_jeu:
					print (f"Vous avez entrer '{len(lettre_entrer)}' lettres au lieu d'une seule lettre . Il vous reste '{nbre_chance}' Chances ")
				lettre_entrer = input("Veillez svp entrer une seule lettre: ")

			if len (lettre_entrer) == 0:#Si le joueur n'a rien entré comme lettre
				if nbre_chance == Dn.fin_jeu:
					print (f"Jeu terminé. Vous n'avez pas pu deviner le mot.\nLe mot à deviner était '{mot_au_hazart}' ")
				elif nbre_chance > Dn.fin_jeu:
					print (f"Vous avez entrer une lettre vide. Il vous reste '{nbre_chance}' Chances ")
				lettre_entrer = input("Veillez entrer une lettre SVP: ")

		if lettre_entrer in mot_au_hazart:#Vérification de gain
			retour = list()
			mot_trouver.append(lettre_entrer)
			for lettre in mot_au_hazart:
				if lettre not in mot_trouver:
					lettre = '*'
				retour.append(lettre)
				mot_trouver_ = ''.join(retour)
			if mot_trouver_ == mot_au_hazart:
				score += nbre_chance
				print (f"Félicitation. Vous avez réussi à trouver \ntoutes les Lettres du mot. Le mot à deviner était '{mot_au_hazart}'.\
					\nVous avez gagner '{nbre_chance}' points. Votre nouveau score est de '{score}'")
			else:
				print (f"Réjouissez-vous. Votre refflexion a porter de fruit. Vous \nVous avez trouver la lettre '{lettre_entrer}' du mot.\
				\nVotre mot a deviner: {retour}")

		elif lettre_entrer not in mot_au_hazart:#Vérification d'échoue
			nbre_chance -= Dn.diminution_de_chance
			if nbre_chance == Dn.fin_jeu:
				print (f"Jeu terminé. Vous n'avez pas pu deviner le mot.\nLe mot à deviner était '{mot_au_hazart}' ")
			elif nbre_chance > Dn.fin_jeu:
				print (f"Vous avez entrer une mauvaise lettre cette fois-ci. Il vous reste '{nbre_chance}' Chances ")
	return score
#Programme du jeu en bonne et du forme. Il prend le score et le mot a deviner en paramètre et renvoie le score final après le jeux.

def information():
	nom = input("Veillez saisire votre prenom SVP: ")
	nom.lower()
	Repertoire = lir_fichier_b('SCORES')
	if nom in Repertoire.keys(): #Anciens joueur
		print (f"Soyez les bienvenues {nom.capitalize()}. Votre anciens score est {Repertoire[nom]}")
		score =  Repertoire[nom]
	else:#Nouveau joueur
		print (f"Bonjour {nom.capitalize()}. Votre score actuel est '0'. Bonne chance a vous.")
		score = Dn.score_initial
		Repertoire[nom] = score
		ouvrir_fichier_b("SCORES",Repertoire)
	return nom.lower(), score
#Programme de receuil des informations sur le joueur. Retourn le nom et le score initial du joueur

def Score_(nom,n_score):
	dic = lir_fichier_b("SCORES")#recupération du dictionnaire des joueurs
	dic [nom] = n_score#mise a jour
	ouvrir_fichier_b("SCORES",dic)#enrégistrement
	return lir_fichier_b("SCORES")[nom]
#permet de mettre a jour le score du joueur.