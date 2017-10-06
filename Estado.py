from Ambiente import Ambiente

class Estado:
	estados_possiveis = []
	estado_pai = []
	def explora_no(self):  # visualizar os estados possiveis a partir do atual
		
		self.estados_possiveis = [] # limpando os estados possiveis para que nao tenha conteudo de um no anterior
		
		if(self.atual.getLocal_especifico(self.pos_x,self.pos_y) != None):
			if(self.atual.getLocal_especifico(self.pos_x,self.pos_y).sujo == True): # proximo estado pode ser o meu quadrado limpo?
				est_auxiliar = Estado(self.atual.num_quadrados,self.pos_x,self.pos_y)
				est_auxiliar.atual = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
				est_auxiliar.atual.getLocal_especifico(self.pos_x,self.pos_y).limpa() # e limpa o meu quadrado nesse estado possivel gerado (est_aux)
				est_auxiliar.setPai(self)
				self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis

		if(self.atual.getLocal_especifico(self.pos_x+1,self.pos_y) != None):
			est_auxiliar = Estado(self.atual.num_quadrados,self.pos_x+1,self.pos_y)
			est_auxiliar.atual = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
			est_auxiliar.setPai(self)
			self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis

		if(self.atual.getLocal_especifico(self.pos_x-1,self.pos_y) != None):
			est_auxiliar = Estado(self.atual.num_quadrados,self.pos_x-1,self.pos_y)
			est_auxiliar.atual = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
			est_auxiliar.setPai(self)
			self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis
		
		if(self.atual.getLocal_especifico(self.pos_x,self.pos_y+1) != None):	
			est_auxiliar = Estado(self.atual.num_quadrados,self.pos_x,self.pos_y+1)
			est_auxiliar.atual = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
			est_auxiliar.setPai(self)
			self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis
		
		if(self.atual.getLocal_especifico(self.pos_x,self.pos_y-1) != None):
			est_auxiliar = Estado(self.atual.num_quadrados,self.pos_x,self.pos_y-1)
			est_auxiliar.atual = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
			est_auxiliar.setPai(self)
			self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis

		return self.estados_possiveis

	# ACOES (nunca usar acoes sem antes explorar o no) ============================
	def limpa_atual(self):
		self.atual.getLocal_especifico(self.pos_x,self.pos_y).limpa()

	def andar_para_cima(self):
		if(self.pos_y+1 <= self.atual.ry):
			for e in self.estados_possiveis:
				if(e.pos_y == self.pos_y+1 and e.pos_x == self.pos_x):
					return e

			prox_estado = Estado(self.atual.num_quadrados,self.pos_x,self.pos_y+1)
			prox_estado.atual = self.copy(self.atual)
			prox_estado.setPai(self)
			return prox_estado

	def andar_para_baixo(self):
		if(self.pos_y-1 >= 0):
			for e in self.estados_possiveis:
				if(e.pos_y == self.pos_y-1 and e.pos_x == self.pos_x):
					return e

			prox_estado = Estado(self.atual.num_quadrados,self.pos_x,self.pos_y-1)
			prox_estado.atual = self.copy(self.atual)
			prox_estado.setPai(self)
			return prox_estado

	def andar_para_esquerda(self):
		if(self.pos_x-1 >= 0):
			for e in self.estados_possiveis:
				if(e.pos_y == self.pos_y and e.pos_x == self.pos_x-1):
					return e

			prox_estado = Estado(self.atual.num_quadrados,self.pos_x-1,self.pos_y)
			prox_estado.atual = self.copy(self.atual)
			prox_estado.setPai(self)
			return prox_estado

	def andar_para_direita(self):
		if(self.pos_x+1 <= self.atual.rx):
			for e in self.estados_possiveis:
				if(e.pos_y == self.pos_y and e.pos_x == self.pos_x+1):
					return e

			prox_estado = Estado(self.atual.num_quadrados,self.pos_x+1,self.pos_y)
			prox_estado.atual = self.copy(self.atual)
			prox_estado.setPai(self)
			return prox_estado

	#==============================================================================
	
	def verifica_objetivo(self):
		count = 0
		for q in self.atual.locais:
			if(q.sujo == False):
				count = count + 1
		
		if(count == self.atual.num_quadrados):
			return True 
		else:
			return False

	def setPai(self,pai):
		self.estado_pai = pai

	def getPai(self):
		return self.estado_pai

	def visualizar_estado(self,est):
		for e in est.atual.locais:
			print "[ x:"+str(e.x)+" y: "+str(e.y)+" sujo: "+str(e.sujo)+" ]"
		print "[Agente: x:" +str(est.pos_x)+ " y:" + str(est.pos_y) + "]\n"

	def visualizar_estado_atual(self):
		for e in self.atual.locais:
			if(self.pos_x == e.x and self.pos_y == e.y):
				print "- - - - - - - - - - - - "
				print "| x:"+str(e.x)+" y: "+str(e.y)+" sujo: "+str(e.sujo)+" |"
				print "- - - - - - - - - - - - "
			else:
				print "[ x:"+str(e.x)+" y: "+str(e.y)+" sujo: "+str(e.sujo)+" ]"
	
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

	def __init__(self,num_quadrados,pos_do_asp_X,pos_do_asp_Y):
		self.atual = Ambiente(num_quadrados)
		self.pos_x = pos_do_asp_X
		self.pos_y = pos_do_asp_Y
		self.estado_pai = None