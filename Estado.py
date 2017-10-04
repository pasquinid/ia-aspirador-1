from Ambiente import Ambiente
class Estado:
	estados_possiveis = []

	def explora_no(self):  # visualizar os estados possiveis a partir do atual
		
		self.estados_possiveis = [] # limpando os estados possiveis para que nao tenha conteudo de um no anterior
		
		if(self.atual.getLocal_especifico(self.pos_x,self.pos_y) != None):
			if(self.atual.getLocal_especifico(self.pos_x,self.pos_y).sujo == True): # proximo estado pode ser o meu quadrado limpo?
				est_auxiliar = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
				est_auxiliar.getLocal_especifico(self.pos_x,self.pos_y).limpa() # e limpa o meu quadrado nesse estado possivel gerado (est_aux)
				self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis

		if(self.atual.getLocal_especifico(self.pos_x+1,self.pos_y) != None):
			if(self.atual.getLocal_especifico(self.pos_x+1,self.pos_y).sujo == True): # proximo estado pode ser o quadrado A MINHA DIREITA limpo?
				est_auxiliar = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
				est_auxiliar.getLocal_especifico(self.pos_x+1,self.pos_y).limpa() # e limpa o meu quadrado nesse estado possivel gerado (est_aux)
				self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis

		if(self.atual.getLocal_especifico(self.pos_x-1,self.pos_y) != None):
			if(self.atual.getLocal_especifico(self.pos_x-1,self.pos_y).sujo == True): # proximo estado pode ser o quadrado A MINHA ESQUERDA limpo?
				est_auxiliar = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
				est_auxiliar.getLocal_especifico(self.pos_x-1,self.pos_y).limpa() # e limpa o meu quadrado nesse estado possivel gerado (est_aux)
				self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis
		
		if(self.atual.getLocal_especifico(self.pos_x,self.pos_y+1) != None):	
			if(self.atual.getLocal_especifico(self.pos_x,self.pos_y+1).sujo == True): # proximo estado pode ser o quadrado A CIMA limpo?
				est_auxiliar = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
				est_auxiliar.getLocal_especifico(self.pos_x,self.pos_y+1).limpa() # e limpa o meu quadrado nesse estado possivel gerado (est_aux)
				self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis
		
		if(self.atual.getLocal_especifico(self.pos_x,self.pos_y-1) != None):
			if(self.atual.getLocal_especifico(self.pos_x,self.pos_y-1).sujo == True): # proximo estado pode ser o quadrado A BAIXO limpo?
				est_auxiliar = self.copy(self.atual) # sim , entao copia o estado (ambiente) atual e..
				est_auxiliar.getLocal_especifico(self.pos_x,self.pos_y-1).limpa() # e limpa o meu quadrado nesse estado possivel gerado (est_aux)
				self.estados_possiveis.append(est_auxiliar) #adiciona ele aos estados possiveis

		return self.estados_possiveis

	# ACOES (nunca usar acoes sem antes explorar o no) ============================
	def andar_para_cima(self):
		self.atual = self.copy(self.atual) 
		self.pos_y = self.pos_y+1
		self.atual.getLocal_especifico(self.pos_x,self.pos_y).limpa()


	def andar_para_baixo(self):
		self.atual = self.copy(self.atual) 
		self.pos_y = self.pos_y-1
		self.atual.getLocal_especifico(self.pos_x,self.pos_y).limpa()


	def andar_para_esquerda(self):
		self.atual = self.copy(self.atual) 
		self.pos_x = self.pos_x-1
		self.atual.getLocal_especifico(self.pos_x,self.pos_y).limpa()


	def andar_para_direita(self):
		self.atual = self.copy(self.atual) 
		self.pos_x = self.pos_x+1
		self.atual.getLocal_especifico(self.pos_x,self.pos_y).limpa()
	#==============================================================================
	def visualizar_estado(self,amb):
		for e in amb.locais:
			print "[ x:"+str(e.x)+" y: "+str(e.y)+" sujo: "+str(e.sujo)+" ]"	

	def visualizar_estado_atual(self):
		for e in self.atual.locais:
			if(self.pos_x == e.x and self.pos_y == e.y):
				print "- - - - - - - - - - - - "
				print "| x:"+str(e.x)+" y: "+str(e.y)+" sujo: "+str(e.sujo)+" |"
				print "- - - - - - - - - - - - "
			else:
				print "[ x:"+str(e.x)+" y: "+str(e.y)+" sujo: "+str(e.sujo)+" ]"
	
	def copy(self,Amb):
		novo_amb = Ambiente(int(Amb.getQuadrados()),Amb)
		count = 0

		for l in Amb.getLocais():
			if(l.sujo == True):
				novo_amb.locais[count].sujo = True
			else:
				novo_amb.locais[count].sujo = False
			count = count + 1
		return novo_amb

	def __init__(self,num_quadrados,pos_do_asp_X,pos_do_asp_Y):
		self.atual = Ambiente(num_quadrados,'raiz')
		self.pos_x = pos_do_asp_X
		self.pos_y = pos_do_asp_Y