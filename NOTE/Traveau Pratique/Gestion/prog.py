#Coding:utf-8

class essaie:
	a = 0
	def __init__(self,v1,v2):
		essaie.a += 1
		self.v1 = v1
		self.v2 = v2
		self._xi = "75 84 59 7 4 5 11 33 557 8 99 5 41 22 55 66 33 11 5 8 9 5 4 2 4 8 8 9 7 4 5 7".split(" ")
		self.xi = [int(i) for i in self._xi]
	def addition(cls,v1,v2):
		return v1+v2
	addition = classmethod(addition)

	def calcule(self,signe):
		if signe == '+':
			r = essaie.addition(self.v1,self.v2)
			return r 
	def __repr__(self):
		return f"JE suis {self.v1} "
	
	def __getitem__(self,index):
		return self.xi[index]

p = essaie(49,53)
#print (p)
r = p.calcule('+')
#p.v2 = 60
print (p.v2)
print (p[9])