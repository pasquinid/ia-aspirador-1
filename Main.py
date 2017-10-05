from Estado import *


def estado_existe(estado_possivel, borda):
    for estado_borda in borda:
        if((estado_borda.atual.pos_x == estado_possivel.atual.pos_x) and(estado_borda.atual.pos_y == estado_possivel.atual.pos_y) and (estado_borda.pos_x == estado_possivel.pos_x) and (estado_borda.pos_y == estado_possivel.pos_y) and (estado_borda.atual.sujo == estado_possivel.atual.sujo)):
            return True

    return False


def mostra_caminho(nos_coloridos):
    print "Caminho pecorrido ate objetivo"
    for no_colorido in nos_coloridos:
        no_colorido.visualizar_estado(no_colorido.atual)


def main():
    estado_inicial = Estado(4, 0, 0)
    print "Visualizando estado criado\n"
    estado_inicial.visualizar_estado(estado_inicial)
    lista_estados_possiveis = estado_inicial.explora_no()
    
    print "Visualizando estados possiveis\n"
    for index in lista_estados_possiveis:
        estado_inicial.visualizar_estado(index)


if __name__ == '__main__':
    main()
