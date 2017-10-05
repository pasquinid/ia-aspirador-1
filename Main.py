#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Estado import Estado
from Largura import Largura
import pdb

"""
    Method : estado_existe
    Param: estado_possivel, borda
    Verifica se estado_possivel já existe na borda
"""
def estado_existe(estado_possivel, borda):
    #Acessando os quadrados do estado possivel para comparação
    lst_locais_estado_possivel = estado_possivel.atual.getLocais()
    for estado_borda in borda:
        #Acessando os quadrados do estado na lista da borda para comparação
        lst_locais_borda = estado_borda.atual.getLocais()
        locais_iguais = True
        #Comparação entra os locais do estado presente na borda e do estado possivel
        for index in (0, len(lst_locais_borda) - 1):
            locais_iguais = ((lst_locais_borda[index].x == lst_locais_estado_possivel[index].x) and (lst_locais_borda[index].y == lst_locais_estado_possivel[index].y) and (lst_locais_borda[index].sujo == lst_locais_estado_possivel[index].sujo))
            if (locais_iguais == False):
                break
        
        #Verificando se o estado é realmente igual até na posição do agente
        if(locais_iguais and (estado_borda.pos_x == estado_possivel.pos_x) and (estado_borda.pos_y == estado_possivel.pos_y)):
            return True
    return False

"""
    Method : mostra_caminho
    Param: nos_coloridos
    Imprime o caminho de nós expandidos até o objetivo ou até a borda está vazia
"""
def mostra_caminho(nos_coloridos):
    print "Caminho pecorrido ate objetivo"
    for no_colorido in nos_coloridos:
        no_colorido.visualizar_estado(no_colorido)


def main():
    estado_inicial = Estado(4, 0, 0)
    print "Visualizando estado criado\n"
    estado_inicial.visualizar_estado(estado_inicial)

    largura = Largura(estado_inicial)

    #Enquanto a borda não estiver vazia
    while(largura.borda != []):
        no_explorado = largura.no_explorado()
        #Verifica se o proximo no a ser explorado não é vazio e se ele é um no objetivo
        if((no_explorado != None) and no_explorado.verifica_objetivo()):
            break
        else:
            #se o nó for vazio algo ocorreu de errado
            if(no_explorado == None):
                print "[ERRO] Não foi possivel econtrar a solução"
                break
            #Gera todos os estados possiveis a partir do no explorado
            lst_estados_possiveis = no_explorado.explora_no()
            print "Visualizando estados possiveis\n"
            for index in lst_estados_possiveis:
                index.visualizar_estado(index)
            #Inserção dos nós na borda    
            for estado in lst_estados_possiveis:
                if(not estado_existe(estado, largura.borda)):
                    largura.add_borda(estado)
    #Imprime o caminho
    print "========== Mostrando caminho ================="
    mostra_caminho(largura.nos_coloridos)


if __name__ == '__main__':
    main()
