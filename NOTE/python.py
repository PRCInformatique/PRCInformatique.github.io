#coding:utf-8

def table_multiplication(mlt_de = 1, fin = 12):
	liste = list()
	for mul in range(0,fin+1):
		liste.append(f"{mlt_de} x {mul} = {mlt_de*mul} ")
	return liste

inn = int (input("entrer un nombre entier: "))

A =  (table_multiplication(inn))
for i in A:
	print (i)