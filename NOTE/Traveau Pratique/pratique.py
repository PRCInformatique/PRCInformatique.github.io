#coding:utf-8
import fonction as Ft 

def jeu_pendu():
	quit = ""
	nm,scor = Ft.information()
	while quit.lower() != 'fin':
		mot = Ft.mot_hazart()
		nouveau_score = Ft.mot_avec_lettre(scor,mot)
		scor = Ft.Score_(nm,nouveau_score)
		quit = input("Entrer fin pour quitter le jeu: ")

jeu_pendu()
