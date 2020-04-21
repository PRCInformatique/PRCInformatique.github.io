#coding:utf-8

"""
TP1 Open_classroom
	Le joueur mise sur un numéro compris entre 0 et 49 
	(50 numéros en tout). En choisissant son numéro, il
	 y dépose la somme qu'il souhaite miser.

	La roulette est constituée de 50 cases allant 
	naturellement de 0 à 49. Les numéros pairs sont de 
	couleur noire, les numéros impairs sont de couleur
	 rouge. Le croupier lance la roulette, lâche la 
	 bille et quand la roulette s'arrête, relève le 
	 numéro de la case dans laquelle la bille s'est 
	 arrêtée. Dans notre programme, nous ne reprendrons 
	 pas tous ces détails « matériels » mais ces 
	 explications sont aussi à l'intention de ceux qui 
	 ont eu la chance d'éviter les salles de casino 
	 jusqu'ici. Le numéro sur lequel s'est arrêtée la 
	 bille est, naturellement, le numéro gagnant.

	Si le numéro gagnant est celui sur lequel le 
	joueur a misé (probabilité de 1/50, plutôt faible), 
	le croupier lui remet 3 fois la somme misée.

	Sinon, le croupier regarde si le numéro misé par 
	le joueur est de la même couleur que le numéro 
	gagnant (s'ils sont tous les deux pairs ou tous 
	les deux impairs). Si c'est le cas, le croupier 
	lui remet 50 % de la somme misée. Si ce n'est pas 
	le cas, le joueur perd sa mise.
	def paire (chiffre):
		if chiffre%2 == 0:
			paire = True
		if chiffre%2 == 1:
			paire = False
		return paire

	def Noire (N_gagnant, N_jouer):
		if paire(N_gagnant) == True and paire (N_jouer) == True:
			return True
		return False

	def Rouge (N_gagnant, N_jouer):
		if paire(N_gagnant) == False and paire (N_jouer) == False:
			return True
		return False

	def gain (N_gagnant,N_jouer,mise):
		ga = 0
		if N_gagnant == N_jouer:
			ga = mise + mise * 3
		if Noire(N_gagnant,N_jouer) == True or Rouge(N_gagnant,N_jouer) == True:
			ga = mise + mise *50/100
		return ga

	def depot ():
		depo = input("Charger votre port monaie: ")
		depo = int (depo)
		return depo

	def Zcasino():
		porte_monnaie = depot()
		retour = ""
		while porte_monnaie > 0 and retour != 'Off' or 'off':
			Numero_jouer = input ("Entrer un numero compris entre 0 et 50: ")
			Numero_jouer = int (Numero_jouer)
			while 0<Numero_jouer>50:
				Numero_jouer = input ("Entrer un numero compris entre 0 et 50: ")
				Numero_jouer = int (Numero_jouer)
			Mise = input ("Entrer votre montant de mise: ")
			Mise = int (Mise)
			porte_monnaie -= Mise
			print (f"Nouveau solde: {porte_monnaie}")
			import random 
			Numero_gagnant = random.randrange(50)
			print (f"Numéro gagnant: {Numero_gagnant}")
			ga = gain(Numero_gagnant,Numero_jouer,Mise)
			porte_monnaie += ga
			revenu = f"Vous avez gagner: {ga}"
			print (revenu,f"Votre solde est de: {porte_monnaie}")
			if porte_monnaie <=30:
				Port = input ("Veillez Entrer 'Recharge' pour charger voter porte monnaie: ")
				if Port == 'Recharge':
					P = depot()
					porte_monnaie += P
			retour = input ("Entrer sur 'Off' pour quitter cliquer 'Entrer' pour continuer: ")

	Zcasino()

"""
import exo

dic = {
	"marque":"Itel S35",
	"type_de_connexion":'4G',
	"memoire_rom":'64GB',
	'memoire_ram':'8gb',
	"processeur":'34m',
	'version':'dav+1.0'
}

Itel = exo.SmartPhone(**dic)
cara = Itel.marque
print (cara)