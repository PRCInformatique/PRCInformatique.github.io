#Coding:utf-8

class essaie:
	a = 0
	def __init__(self,v1,v2):
		essaie.a += 1
		self.v1 = v1
		self.v2 = v2
	def addition(cls,v1,v2):
		return v1+v2
	addition = classmethod(addition)
	def sustration(v1,v2):
		return v1-v2
	sustration = staticmethod(sustration)
	def calcule(self,signe):
		if signe == '+':
			r = essaie.addition(self.v1,self.v2)
			return r 
	def __repr__(self):
		return f"JE suis {self.v1} "
	def __setattr__(self,nom,valeur):
		valeur+=valeur
		object.__setattr__(self,nom,valeur)
p = essaie(49,53)
#print (p)
r = p.calcule('+')
#p.v2 = 60
print (p.v2)
print (r)