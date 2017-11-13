
import numpy as np

from FuzzyImpl1.GrauMancha import GrauMancha
from FuzzyImpl1.GrauSujeira import GrauSujeira

m = GrauMancha()
s = GrauSujeira()
enter =0
def main():
    print(" Welcome! \n  The Fuzzy Program\n")
    while (1):
        print(" Choose one option bellow:")
        print("1- Calc one Relevance:")
        print("2- Calc interval Of Relance:")
        print("3- Print interval of suport by group:")
        print("4- Print interval of core by group:")



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
    if group == "Baixo":
        return calOfRelevenceTriagle(0, 0, 50, value)
    if group == "Medio":
        return calOfRelevenceTriagle(0, 50, 100, value)
    if group == "Alto":
        return calOfRelevenceTriagle(50, 100, 100, value)
    else:
        print("Group not Found->" + group)




def calcRelevance(value):
    if isfloat(value):
        value = float(value)
        m.sm = calOfRelevenceTriagle(1, 1, 1.5, value)
        m.mm = calOfRelevenceTriagle(1, 1.5, 2.0, value)
        m.gm = calOfRelevenceTriagle(1.65, 2.0, 2.0, value)

        s.ps = calOfRelevenceTriagle(1, 1, 1.5, value)
        s.ms = calOfRelevenceTriagle(1, 1.5, 2.0, value)
        s.gs = calOfRelevenceTriagle(1.65, 2.0, 2.0, value)


def baseRegras():

    if(s.ps > 0 and m.sm > 0):
        return 'mc'
    if(s.ms > 0 and m.sm > 0):
        return 'c'
    if(s.gs > 0 and m.sm > 0):
        return 'm'
    if(s.ps > 0 and m.mm > 0):
        return 'm'
    if(s.ms > 0 and m.mm > 0):
        return 'm'
    if(s.gs > 0 and m.mm > 0):
        return 'l'
    if(s.ps > 0 and m.gm > 0):
        return 'l'
    if(s.ms > 0 and m.gm > 0):
        return 'l'
    if(s.gs > 0 and m.gm > 0):
        return 'ml'




def calcRelavanceOptionTwo():
    value = raw_input("Type the interval: ")
    value1 = raw_input("Type the interval: ")
    step = raw_input("Type the step: ")
    group = raw_input("Type the group: ")
    if (isfloat(value) and isfloat(value1) and isfloat(step)):
        value = float(value)
        value1 = float(value1)
        step = float(step)
        results = list()
        array = np.arange(value, value1, step)
        for x in range(0, len(array)):
            results.append(calcByGroup(group, array[x]))

        twodecimals = ["%.2f".strip("\'") % v for v in results]
        print(array)
        print(twodecimals)


def calcRelavanceOptionTwoTra():
    value = raw_input("Type the interval: ")
    value1 = raw_input("Type the interval: ")
    step = raw_input("Type the step: ")
    group = raw_input("Type the group: ")
    if (isfloat(value) and isfloat(value1) and isfloat(step)):
        value = float(value)
        value1 = float(value1)
        step = float(step)
        results = list()
        array = np.arange(value, value1, step)
        for x in range(0, len(array)):
            results.append(calcByGroupTra(group, array[x]))

        twodecimals = ["%.2f".strip("\'") % v for v in results]
        print(array)
        print(twodecimals)


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        print("Try a valid number Like 1 or 1.0")
        return False


# Imprima na tela o intervalo  correspondente ao suporte do conjunto escolhido

def printInterval():
    group = raw_input("Type the group: ")
    if group == "Baixo":
        supportBaixo()
    if group == "Medio":
        supportMedio()
    if group == "Alto":
        supportAlto()
    else:
        print("Group not Found->" + group)

 #Imprima na tela o intervalo correspondente ao ncleo do conjunto escolhido

def printCore():
    group = raw_input("Type the group: ")
    if str(group) == "Baixo":
        coreBaixo()
    if group == "Medio":
        coreMedio()
    if group == "Alto":
        coreAlto()
    else:
        print("Group not Found->" + group)


def supportBaixo():
    count = 1
    suportInf = 0
    suportSup = 0
    trigSup = True
    trigInf = True

    while (count < 2):
        count = count + 0.00001
        x = calOfRelevenceTriagle(1, 1, 1.5, count)
        if (x >= 0.999):
            suportInf = count
            break;

    count = 1
    while (count < 2):
        count = count + 0.00001
        x = calOfRelevenceTriagle(1, 1, 1.5, count)
        if (x <= 0.001):
            suportSup = count
            break;

    if suportInf > suportSup:
        print("[" + str(suportSup) + " , " + str(suportInf) + "]")
    else:
        print("[" + str(suportInf) + " , " + str(suportSup) + "]")


def supportMedio():
    count = 1
    suportInf = 0
    suportSup = 0
    trigSup = True
    trigInf = True
    while (count < 2):
        count = count + 0.00001
        x = calOfRelevenceTriagle(1, 1.5, 2.0, count)
        if (x >= 0.999):
            suportInf = count
            break;

    count = 1
    while (count < 2):
        count = count + 0.00001
        x = calOfRelevenceTriagle(1, 1.5, 2.0, count)
        if (x >= 0.001):
            suportSup = count
            break;

    if suportInf > suportSup:
        print("[" + str(suportSup) + " , " + str(suportInf) + "]")
    else:
        print("[" + str(suportInf) + " , " + str(suportSup) + "]")


def supportAlto():
    count = 1
    suportInf = 0
    suportSup = 0
    trigSup = True
    trigInf = True
    while (count < 2):
        count = count + 0.00001
        x = calOfRelevenceTriagle(1.65, 2.0, 2.0, count)
        if (x >= 0.999):
            suportInf = count
            break;

    count = 1
    while (count < 2):
        count = count + 0.00001
        x = calOfRelevenceTriagle(1.65, 2.0, 2.0, count)
        if (x >= 0.001):
            suportSup = count
            break;

    if suportInf > suportSup:
        print("[" + str(suportSup) + " , " + str(suportInf) + "]")
    else:
        print("[" + str(suportInf) + " , " + str(suportSup) + "]")


def coreBaixo():
    count = 1
    suportInf = 0
    suportSup = 0
    trigSup = True
    trigInf = False
    while (count < 2):
        count = count + 0.0001
        x = calOfRelevenceTriagle(1, 1, 1.5, count)
        if (0.99999 < x <= 1):
            suportInf = count
            while (count < 2):
                count = count + 0.0001
                x = calOfRelevenceTriagle(1, 1, 1.5, count)
                if (0.99999 < x <= 1):
                    suportSup = count
                else:
                    suportSup = count
                    trigInf = True
                    break;

        if trigInf==True:
            break;


    if suportInf > suportSup:
        print("[" + str(suportSup) + " , " + str(suportInf) + "]")
    else:
        print("[" + str(suportInf) + " , " + str(suportSup) + "]")


def coreMedio():
    count = 1
    suportInf = 0
    suportSup = 0
    trigSup = True
    trigInf = False
    while (count < 2):
        count = count + 0.0001
        x = calOfRelevenceTriagle(1, 1.5, 2.0, count)
        if (0.99999 < x <= 1):
            suportInf = count
            while (count < 2):
                count = count + 0.0001
                x = calOfRelevenceTriagle(1, 1.5, 2.0, count)
                if (0.99999 < x <= 1):
                    suportSup = count
                else:
                    suportSup = count
                    trigInf = True
                    break;

        if trigInf==True:
            break;

def coreAlto():

    count = 1
    suportInf = 0
    suportSup = 0
    trigSup = True
    trigInf = False
    while (count < 2):
        count = count + 0.0001
        x = calOfRelevenceTriagle(1.65, 2.0, 2.0, count)
        if (0.99999 < x <= 1):
            suportInf = count
            while (count < 2):
                count = count + 0.0001
                x =calOfRelevenceTriagle(1.65, 2.0, 2.0, count)
                if (0.99999 < x <= 1):
                    suportSup = count
                else:
                    suportSup = count
                    trigInf = True
                    break;

            if trigInf == True:
                break;

    if suportInf > suportSup:
        print("[" + str(suportSup) + " , " + str(suportInf) + "]")
    else:
        print("[" + str(suportInf) + " , " + str(suportSup) + "]")





if __name__ == '__main__':
    main()
