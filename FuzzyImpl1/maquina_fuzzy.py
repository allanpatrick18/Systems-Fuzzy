
import numpy as np

import matplotlib.pyplot as plt
from FuzzyImpl1.GrauMancha import GrauMancha
from FuzzyImpl1.GrauSujeira import GrauSujeira
from FuzzyImpl1.TempoLavagem import TempoLavagem

m = GrauMancha()
s = GrauSujeira()
time  = TempoLavagem()
saida = {'mc': [], 'c':[],'m':[],'l':[], 'ml':[]}
ativacao = {'1': 0, '2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
regras = {'1':'m','2':'mc','3':'m','4':'m','5':'m','6':'l','7':'l','8':'l','9':'ml'}
conjuntosConsequentes = {'mc', 'c', 'm', 'l', 'ml'}
enter =0
x =60
y=70
def main():
    print(" Welcome! \n  The Fuzzy Program\n")
    while (1):
        print(" Choose one option bellow:")
        print("1- Calc one Relevance:")
        print("2- Calc interval Of Relance:")
        print("3- Print interval of suport by group:")
        print("4- Print interval of core by group:")
       # plotConjuntos()
        pertineciaMacha(x)
        pertinenciaSugeira(y)
        baseRegras()
        verificarMesmaSaidaAtivadas()
        agregacaoRegras()

def calOfRelevenceTriagle(a, m, b, x):
    if (x <= a):
        return 0
    elif (a < x <= m):
        return (x - a) / (m - a)
    elif (m < x <= b):
        return (b - x) / (b - m)
    else:
        return 0

def calcByGroup(group, value):
    if group == "sm":
        return calOfRelevenceTriagle(0, 0, 50, value)
    if group == "mm":
        return calOfRelevenceTriagle(0, 50, 100, value)
    if group == "gm":
        return calOfRelevenceTriagle(50, 100, 100, value)
    else:
        print("Group not Found->" + group)





def pertineciaMacha(value):

    value = float(value)
    m.sm = calOfRelevenceTriagle(1, 1, 50, value)
    m.mm = calOfRelevenceTriagle(1, 50, 100, value)
    m.gm = calOfRelevenceTriagle(50, 100, 100, value)

def pertinenciaSugeira(value):
    value = float(value)
    s.ps = calOfRelevenceTriagle(1, 1, 50, value)
    s.ms = calOfRelevenceTriagle(1, 50, 100, value)
    s.gs = calOfRelevenceTriagle(50, 100, 100, value)

def calcConsequente(group,value):
        value = float(value)
        if group == "mc":
            return calOfRelevenceTriagle(1, 1, 10, value)
        if group == "c":
            return calOfRelevenceTriagle(1, 10, 25, value)
        if group == "m":
            return calOfRelevenceTriagle(10, 25, 40, value)
        if group == "l":
            return calOfRelevenceTriagle(25, 40, 60, value)
        if group == "ml":
            return calOfRelevenceTriagle(40, 60, 60, value)


def compSupTmim(value, value1):
    if(value>=value1):
        return value1
    else:
        return value

def plotConjuntos():
    poligono_ps =[]
    poligono_mm = []
    poligono_gm = []
    universodiscreto = np.arange(1,100,1)
    for x in universodiscreto:
        if(x<50):
            poligono_ps.append(calcByGroup("sm",x))
        if(50>x):
            poligono_gm.append(calcByGroup("mm", x))

        poligono_mm.append(calcByGroup("gm", x))

    plt.plot(poligono_ps)
    plt.plot(poligono_gm)
    plt.plot(poligono_mm)


def baseRegras():

    if(s.ps > 0 and m.sm > 0):
        saida['mc'].append(compSupTmim(s.ps,m.sm))

    if(s.ms > 0 and m.sm > 0):
        saida['c'].append( compSupTmim(s.ms, m.sm))

    if(s.gs > 0 and m.sm > 0):
        saida['m'].append(compSupTmim(s.gs, m.sm))

    if(s.ps > 0 and m.mm > 0):
        saida['m'].append(compSupTmim(s.ps, m.mm))

    if(s.ms > 0 and m.mm > 0):
        saida['m'].append(compSupTmim(s.ms, m.mm))

    if(s.gs > 0 and m.mm > 0):
        saida['l'].append(compSupTmim(s.gs, m.mm))

    if(s.ps > 0 and m.gm > 0):
        saida['l'].append(compSupTmim(s.ps, m.gm))

    if(s.ms > 0 and m.gm > 0):
        saida['l'].append( compSupTmim(s.ms, m.gm))

    if(s.gs > 0 and m.gm > 0):
        saida['ml'].append( compSupTmim(s.ps, m.gm))



def verificarMesmaSaidaAtivadas():
    if(saida["m"]):
        time.m = min(saida["m"])
    if (saida["mc"]):
        time.mc =min(saida["mc"])
    if (saida["c"]):
        time.c = min(saida["c"])
    if (saida["l"]):
        time.l = min(saida["l"])
    if (saida["ml"]):
        time.ml =min(saida["ml"])

def verificarMinimoMesmaSaida(value1,value2):
     if(value1>=value2):
        return value2
     else:
        return value2

def agregacaoRegras():
    poligonos= []
    for var in conjuntosConsequentes:
        if (saida[var]):
           poligonos.append(semanticaDaRegra(var, max(saida[var])))

    total = [0.0]*len(poligonos[0])
    for a in poligonos:
        total = list(map(max, zip(total, a)))

    return centroide(total)

def maxAgregacao(value, value1):
    if(value > value1):
       return value
    else:
       return value1

def semanticaDaRegra(conjunto, pertinecia):
    poligono_discreto =[]
    universodiscreto = np.arange(1,60,0.01)
    for x in universodiscreto:
              poligono_discreto.append(mandani(pertinecia,calcConsequente(conjunto,x)))

    plt.plot(poligono_discreto)
    # plt.plot(universodiscreto,poligono_discreto)
    return poligono_discreto


def mandani(value1, value2):
    if (value1 >= value2):
        return value2
    else:
        return value1


def centroide(poligono):
     i=0
     nume=0.0
     deno=0.0
     for x in  poligono:
         v = x*i
         nume = nume+v
         deno = deno+x
         i=i+0.01
     result= nume/deno
     print(result)
     plt.plot(poligono)
     return result





def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        print("Try a valid number Like 1 or 1.0")
        return False




if __name__ == '__main__':
    main()
