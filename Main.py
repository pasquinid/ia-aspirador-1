#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Estado import Estado
from Largura import Largura
from Profundidade import Profundidade
from Astar import Astar


"""
    Method : estado_existe
    Param: estado_possivel, borda
    Verifica se estado_possivel já existe na borda
"""
def estado_existe(estado_possivel, borda, coloridos, star):
    #Acessando os quadrados do estado possivel para comparação
    lst_locais_estado_possivel = estado_possivel.atual.locais
    for estado_borda in borda:
        cont = 0
        #Acessando os quadrados do estado na lista da borda para comparação
        lst_locais_borda = estado_borda.atual.locais
        locais_iguais = True
        #Comparação entra os locais do estado presente na borda e do estado possivel
        if not len(lst_locais_borda) == len(lst_locais_estado_possivel):
            continue

        for index in range(0, len(lst_locais_borda)):
            pos_x = lst_locais_borda[index].x == lst_locais_estado_possivel[index].x
            pos_y = lst_locais_borda[index].y == lst_locais_estado_possivel[index].y
            sujo = lst_locais_borda[index].sujo == lst_locais_estado_possivel[index].sujo
            if(pos_x == True and pos_y == True and sujo == True):
                cont = cont + 1

        #Verificando se o estado é realmente igual até na posição do agente
        pos_agente = estado_borda.pos_x == estado_possivel.pos_x and estado_borda.pos_y == estado_possivel.pos_y
        #print "X: " + str(pos_x) + " Y:" + str(pos_y) + " SUJO: " + str(sujo) + " agente: " + str(pos_agente)
        if cont == len(lst_locais_borda) and pos_agente:
            # print "\nTRUE"
            #verifica se o no pertence a borda
            if(coloridos == 0 and star == 1):
                #se o custo do estado possivel for menor que o custo do estado presente na borda, atualiza as informações
                if(estado_borda.f  > estado_possivel.f):
                    estado_borda.estado_pai = estado_possivel.estado_pai
                    estado_borda.h = estado_possivel.h
                    estado_borda.g = estado_possivel.g
                    estado_borda.f = estado_possivel.f
            return True
    #print "\nFALSE"
    return False

def mostra_caminho(nos_coloridos):
    no_objetivo = None
    caminho = []
    for no in nos_coloridos:
        if(no.verifica_objetivo()):
            no_objetivo = no
            break
    if(no_objetivo == None):
        print "Objetivo não encontrado!\n"
        return
    else:
        caminho.append(no_objetivo)

        while(no_objetivo.getPai() != None):
            caminho.append(no_objetivo.getPai())
            no_objetivo = no_objetivo.getPai()

        for no in reversed(caminho):
             no.visualizar_estado(no)


"""
    Method : mostra_expandidos
    Param: nos_coloridos
    Imprime o caminho de nós expandidos até o objetivo ou até a borda está vazia
"""
def mostra_expandidos(nos_coloridos):
    for no_colorido in nos_coloridos:
        no_colorido.visualizar_estado(no_colorido)

def processa_nos(busca, astar):
    #Enquanto a borda não estiver vazia
    while(busca.borda != []):
        no_explorado = busca.no_explorado()
        #Verifica se o proximo no a ser explorado não é vazio e se ele é um no objetivo
        if(no_explorado.verifica_objetivo()):
            break
        else:
            #se o nó for vazio algo ocorreu de errado
            if(no_explorado == None):
                print "[ERRO] Não foi possivel econtrar a solução"
                break
            #Gera todos os estados possiveis a partir do no explorado
            # print "NÓ A SER EXPANDIDO"
            # no_explorado.visualizar_estado(no_explorado)
            lst_estados_possiveis = no_explorado.explora_no()
            # print "Visualizando estados possiveis\n"
            # for index in lst_estados_possiveis:
            #     index.visualizar_estado(index)
            #Inserção dos nós na borda    
            for estado in lst_estados_possiveis:
                show = False
                if(estado_existe(estado, busca.nos_coloridos, 1, astar)):
                    continue
                if estado_existe(estado, busca.borda, 0, astar):
                   pass
                else:
                    busca.add_borda(estado)

    #Imprime o caminho
    # print "========== Mostrando nos expandidos ============"
    # mostra_expandidos(busca.nos_coloridos)

    print "=========Mostrando Caminho ====================="
    mostra_caminho(busca.nos_coloridos)

def main():
    estado_inicial = Estado(4, 0, 0)
    print "Visualizando estado criado\n"
    estado_inicial.visualizar_estado(estado_inicial)

    largura = Largura(estado_inicial)

    print "=======Busca em largura=========\n"
    processa_nos(largura, 0)
    print "Numero de nós gerados: " + str(len(largura.borda) + len(largura.nos_coloridos))

    profundidade = Profundidade(estado_inicial)

    print "======Busca em Profundidade=====\n"
    processa_nos(profundidade, 0)
    print "Numero de nós gerados: " + str(len(profundidade.borda) + len(profundidade.nos_coloridos))

    astar = Astar(estado_inicial)
    print "======Busca Astar=================\n"
    processa_nos(astar, 1)
    print "Numero de nós gerados: " + str(len(astar.borda) + len(astar.nos_coloridos))



if __name__ == '__main__':
    main()
