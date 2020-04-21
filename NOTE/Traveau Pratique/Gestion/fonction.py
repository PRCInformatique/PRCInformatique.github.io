#coding:utf-8
#fichier des fonctions
def ouvrir_b(nom,donne):
	import pickle
	with open(f'fichier/{nom}','wb') as fic:
		sau = pickle.Pickler(fic)
		sau.dump(donne)#ouverture de fichier binaire

def lir_b(nom):
	import pickle
	with open(f"fichier/{nom}",'rb') as fic:
		rec = pickle.Unpickler(fic)
		ret = rec.load()
	return(ret)#lecture de fichier binairaire

def verifie_b (nom,donne_par_defaut):
	try:
		lir_b(f"{nom}")
	except: 
		ouvrir_b(f'{nom}',donne_par_defaut)
	return lir_b(F"{nom}")

#----------------- Fonctions de la classe Gestion -------------------
def dic_total_(nom):
	try:
		lir_b(f"dic_{nom}")
	except:
		ouvrir_b(f"dic_{nom}",{})

	return lir_b(f"dic_{nom}")

def lis_total_(nom):
	try:
		lir_b(f"lis_{nom}")
	except:
		ouvrir_b(f"lis_{nom}",[])
	
	return lir_b(f"lis_{nom}")

def sauv_dic_total_(nom,dic_total):
	ouvrir_b(f"dic_{nom}",dic_total)

def sauv_lis_total_(nom,lis_total):
	ouvrir_b(f"lis_{nom}",lis_total)

def histo_dic(nom_objet,flux):
	flux+=nom_objet
	return lir_b(f"dic_{flux}")

def histo_lis(nom_objet,flux):
	flux+=nom_objet
	return lir_b(f"lis_{flux}")

def point(nom_objet,date = ''):#Mega dictionnaire pour le point des entrers et sortie de l'objet
	dic_entre_total = dic_total_(f"entrer{nom_objet}")
	dic_sorti_total = dic_total_(f"sortie{nom_objet}")
	dic_point = {}
	if date == '': #Demande d'un point générale. Le paramètre date n'est pas définie
		for date_entre,date_sorti in zip (dic_entre_total,dic_sorti_total): 
			entrer = []
			sortie = []
			Entre = {}
			Sorti = {}
			for motif_entre,motif_sorti in zip (dic_entre_total[date_entre].keys(),dic_sorti_total[date_sorti].keys()):
				print (motif_sorti)
				valeur_entre = dic_entre_total[date_entre][motif_entre]
				entrer.append(f"{motif_entre} = {valeur_entre}") #Récupération des Entrées

				valeur_sorti = dic_sorti_total[date_sorti][motif_sorti]
				sortie.append(f"{motif_sorti} = {valeur_sorti}") #Récupération des Sorties
			
			Sorti ["Les Sorties Du Jour Sont"] = sortie
			Entre ["Les Entrées Du Jour Sont"] = entrer
			dic_point[date_entre] = Sorti,Entre #Sotckage dans un dictionnaire qui prend en clé la date

	else:#demande d'un point d'un jour particulier. Le paramètre date est définie
		for motif_entre,motif_sorti in zip (dic_entre_total[date].keys(),dic_sorti_total[date].keys()):

			valeur_entre = dic_entre_total[date][motif_entre]
			entrer.append(f"{motif_entre} = {valeur_entre}") #Récupération des Entrées

			valeur_sorti = dic_sorti_total[date][motif_sorti]
			sortie.append(f"{motif_sorti} = {valeur_sorti}") #Récupération des Sorties
			
		Sorti ["Les Sorties Du Jour Sont"] = sortie
		Entre ["Les Entrées Du Jour Sont"] = entrer
		dic_point[date] = Sorti,Entre #Stockage dans un dictionnaire qui prend en clé la date

	return dic_point #retour du dictionnaire

def enre_objet(pseudo,objet): #methode des enrégistrements des objets a gérés
	try:
		ancien = lir_b(f"{pseudo}objets")
	except:
		ouvrir_b(f"{pseudo}objets",[])
		ancien = lir_b(f"{pseudo}objets")
	for ob in ancien:
		if objet != ob:
			ancien.append(objet)

def enre_oj_espace (pseudo,date,dic): # methode de création de d'enrégistrement des espace de travail pour chaque objet
	ancien = verifie_b(f"{pseudo}oj_espace",[])
	print(ancien)
	for i in ancien:
		if i != (date,dic):
			ancien.append(date,dic)

def tri_dans_dic(pseudo): #Méthode permetant de faire le tri des objets dans un dictionnaire selon leur date
	donne = lir_b(f"{pseudo}oj_espace")
	date = ''
	dic = {}
	for Don in donne:
		Date = Don[0]
		if date == Date:
			dic[date].append(Don[1])
		else:
			dic[date]= [Don[1]]
		date = Date
	ouvrir_b(f"{pseudo}G_dic",dic)
	return dic #dictionnaire d'espace de travail général

#argument: dictionaire: dic, date, flux
def receuil (nom_objet,date = "",dic = {},flux = ""):#£Retourne le grand dictionnaire et la grande listes 
	_total = 0
	flux+=nom_objet
	dic_total = dic_total_(flux)#recupération du grand dictionnaire 
	#Ce dictionnaire prend en clé les dates et en valeur le dictionnaire du jour
	#le dictionnaire du jour prend en clé les motifs et en valeur les valeurs
	lis_total = lis_total_(flux)#recupération de la grande liste .
	#Cette liste est une liste des tuples qui contient date et totale du jour
	dic_total[date] = dic
	sauv_dic_total_(flux,dic_total) #Mise a jour du grand dictionnaire
	for cle in dic.keys(): #Calcule du totale du jours
		valeur = dic[cle]
		_total += valeur
	total = (date,_total) #Tuple de date et total du jour 
	ver = verifie(total,lis_total)
	if ver == True:
		pass
	else :
		lis_total.append(total) 
		sauv_lis_total_(flux,lis_total) #Mise à jour de la grande liste
	return dic_total,lis_total
#*******************************************************************

#------------------ Fonction de la classe Connexion -------------------

def lir_identifiant():
	try:
		lir_b("identifiants")
	except:
		ouvrir_b("identifiants",{})
	return lir_b("identifiants")

def verifie(valeur,liste):
	if valeur in liste:
		return True
	else:
		return False

def verifie_egal(valeur1,valeur2):
	if valeur1 == valeur2:
		return True
	else:
		return False

def lir_fic_identifiant():
	return lir_b("lir_fic_identifiant")

def enre_fic_identifiant(dic):
	ouvrir_b("lir_fic_identifiant",dic)

def enr_identifiant(cle,valeur):
	ancien = lir_identifiant()
	ancien [cle]= valeur
	ouvrir_b("identifiants",ancien)
#************************************************************************

#------------------ Fonction de la classe EspaceDeTravail ---------------
"""
def ouvrir_espace_vide(pseudo,objets): #prend en paramètre le pseudo du nouveau et le non de ses objets à gérer introduit sous forme de dictionnaire
	espace = {}
	for cle in objets:
		espace[cle] = []
	enre_espace(f"{pseudo}espace",espace)
	return len(espace)

def lir_espace (pseudo):
	return lir_b(f"{pseudo}espace")

def enre_espace (pseudo,dic):
	try:
		ancien = lir_espace(f"{pseudo}espace")
	except:
		ouvrir_b(f"{pseudo}espace",dic)
		ancien = lir_espace(f"{pseudo}espace")

	objets = lir_b(f"{pseudo}objets")
	for objet in objets:
		pass
"""