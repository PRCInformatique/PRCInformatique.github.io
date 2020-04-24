#Coding:utf-8
import tkinter

# -------------- fonction de conversion ------------------------
def position(valeur,liste):#donne l'indice de valeur dans liste
	a = -1
	for i in liste:
		a += 1
		if i == valeur:
			return a
def position_conv(valeur1,valeur2,liste):#Donne la position du dernier chiffre du nombre a virgule a prendre en compte pour l'arrondissement de la valeur
	a = 0
	for i in liste:
		a +=1
		if i == valeur1 and liste[a] == valeur2:
			return a

def vale (valeur):#Donne la valeur a prendre en compte si le resultat est un nombre a virgule et que le dernier chiffre de la valeur a convertire est "0"
	valeur = str (valeur)
	a = -1
	l1 = [0]* len(valeur)
	for inv in valeur:
		l1[a] = inv
		a -= 1
	for i in l1:
		if i != "0":
			return i

def arrond (valeur,V_conversion): #Permet l'arrondissement du resultat au cas ou le resultat sera un nombre a virgule approsimative
	valeur = str(valeur)
	print(valeur)
	print(V_conversion)
	V_conversion = str(V_conversion)
	V1 = vale(valeur)
	print (V1)
	VC = V_conversion[-1]
	if V1 == VC:
		return V_conversion
	else:
		if len(valeur)<=2:
			indice = position_conv(V1,valeur[-2],V_conversion)
		else:
			indice = position(V1,V_conversion)
		R = V_conversion[:indice+1]
		return R

def conversion(valr,unite_mesure,unite_conversion):#Programme de conversion en bonne et dû forme. prend en charge la règle de convertion de l'unité mètre.
	u = unite_mesure[0]
	unite_conversion = unite_conversion[0]+u
	unit = f"k{u} h{u} da{u} {u} d{u} c{u} m{u}"
	print (unit)
	unit = unit.split()
	indice_u_mesure = position(u,unit)
	indice_u_conversion = position(unite_conversion,unit)
	resultat = (10**(indice_u_conversion - indice_u_mesure) * valr)
	if type (resultat) == float:
		resultat = arrond(valr,resultat)
	return f"{resultat} {unite_conversion}"
#Peut faire aussi pour littre et gramme.
#//////////////////////////////////////////////////////////////////////////////

#----------------- Programmation graphique -----------------------
App = tkinter.Tk()
App.geometry("200x200")
App.title("Conversion")
#7radio button,7label,1Entry, observateur, traceur
#observeur
def observeur(*args):
	convers.set(conversion(valeur.get(),unite_mesure.get(),unite_conversion.get()))
#----------------
#variable
valeur = tkinter.IntVar()
unite_mesure = tkinter.StringVar()
unite_conversion = tkinter.StringVar()
convers = tkinter.StringVar()

#----------------
#Les widgets

valeur.trace("w",observeur)
unite_mesure.trace("w",observeur)
unite_conversion.trace("w",observeur)

sotie1 = tkinter.Message(App, text = "Unité de Mesure")
sotie2 = tkinter.Message(App, text = "Unité de Conversion")
sotie3 = tkinter.Label(App, text = "Valeur")
entre1 = tkinter.Entry(App, textvariable = unite_mesure )
entre2 = tkinter.Entry(App, textvariable = unite_conversion)
entre3 = tkinter.Entry(App, textvariable = valeur)
sorti4 = tkinter.Label(App, textvariable = convers)
#----------------
sotie1.pack()
entre1.pack()
sotie2.pack()
entre2.pack()
sotie3.pack()
entre3.pack()
sorti4.pack()

App.mainloop()