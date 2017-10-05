from Quadrado import Quadrado
import math
import copy
import random

class Ambiente:
	locais = []

	num_quadrados = 0
	


	def getLocal_especifico(self,x,y):
		for i in self.locais:
			if(i.x == x and i.y == y):
				return i

	def getLocais(self):
		return list(self.locais)

	def getQuadrados(self):
		return int(self.num_quadrados)
	
	def __init__(self,num_quadrados):
		
		if(num_quadrados%2 != 0):
			print("Valor impar!")
			return
		self.num_quadrados = num_quadrados
		tam_x = int(math.sqrt(num_quadrados))
		tam_y = num_quadrados - tam_x

		self.rx = range(tam_x)
		self.ry = range(tam_y)

		self.locais = [Quadrado(True,0,0) for i in range(num_quadrados)]
		
		count = 0 
		for x in self.rx:
			print "ambiente.. x= "+str(x)
			for y in self.ry:
				print "ambiente.. y= "+str(y)
				self.locais[count].x = x
				self.locais[count].y = y
				self.locais[count].sujo = random.choice([True, False])
				count = count + 1
