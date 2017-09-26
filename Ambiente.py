from Quadrado import Quadrado
import math
import copy

class Ambiente:
	locais = []
	num_quadrados = 0
	ambiente_pai = []
	def getLocais(self):
		return list(self.locais)

	def getQuadrados(self):
		return int(self.num_quadrados)
	
	def __init__(self,num_quadrados,pai):
		self.ambiente_pai = pai
		if(num_quadrados%2 != 0):
			print("Valor impar!")
			return
		self.num_quadrados = num_quadrados
		tam_x = int(math.sqrt(num_quadrados))
		tam_y = num_quadrados - tam_x

		rx = range(tam_x)
		ry = range(tam_y)
		
		for x in rx:
			for y in ry:
				q = Quadrado(True,x,y)
				self.locais.append(q)

