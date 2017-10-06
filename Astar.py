class Astar(object):
    borda = []
    nos_coloridos = []

    def __init__(self, raiz):
        self.borda.append(raiz)

    def add_borda(self, estado):
        self.borda.append(estado)
    
    def escolhe_no(self):
        escolhido = self.borda[0]
        pos = 0
        for index in range(1, len(self.borda)):
            if (escolhido.f > self.borda[index].f):
                escolhido = self.borda[index]
                pos = index
        self.borda.remove(escolhido)
        return escolhido

    def no_explorado(self):
        no_explorado = self.escolhe_no()
        self.nos_coloridos.append(no_explorado)
        return no_explorado