import Estado

"""
    Classe responsavel pela busca em largura no agente aspirador de pó
"""
class Largura(object):
    borda = []
    nos_coloridos = []

    """
        Method: Inicialização
        arguments: raiz
        Inicializa a lista da borda começando pela raiz
    """

    def __init__(self, raiz):
        self.borda.append(raiz)

    """
    Method: add_borda
    arguments: estado_possivel
        Adciona novos nós (Estados possiveis) com potencial para serem explorados
    """

    def add_borda(self, estado_possivel):
        self.borda.append(estado_possivel)

    """
    Method: no_explorado
    arguments: None
        Adciona no(Proximo estado) na lista de nós coloridos e o retorna para ser verificado se é objetivo e se não for, ser explorado e gerar novos estados possiveis
    """

    def no_explorado(self):
        no_explorar = self.borda.pop(0)
        self.nos_coloridos.append(no_explorar)
        return no_explorar