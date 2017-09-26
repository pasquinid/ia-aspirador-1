class Quadrado:
	sujo = False
	x = 0
	y = 0
	
	def __init__(self,su,xs,ys):
		self.sujo = su
		self.x = xs
		self.y = ys

	def limpa(self):
		self.sujo = True
