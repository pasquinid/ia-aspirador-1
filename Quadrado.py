#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Quadrado:
	sujo = False  # True = tem sujeira , False = nao tem sujeira
	x = 0
	y = 0
	
	def __init__(self,su,xs,ys):
		self.sujo = su
		self.x = xs
		self.y = ys

	def limpa(self):
		self.sujo = False
