from Ambiente import Ambiente
class Estado:

	def copy(self,Amb):
		novo_amb = Ambiente(int(Amb.getQuadrados()))
		count = 0

		for l in Amb.getLocais():
			if(l.sujo == True):
				novo_amb.locais[count].sujo = True
			else:
				novo_amb.locais[count].sujo = False
			count = count + 1

		return novo_amb