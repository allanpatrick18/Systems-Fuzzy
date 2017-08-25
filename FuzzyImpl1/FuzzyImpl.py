
import numpy as np


def main():
    print(" Welcome! \n  The Fuzzy Program\n")
    while (1):
        print(" Choose one option bellow:")
        print("1- Calc one Relevance:")
        print("2- Calc interval Of Relance:")
        print("3- Print interval of suport by group:")
        value = input()
        if (value == str(1)):
            value = input('The higher:')
            calcRelevance(value)
        if (value == str(2)):
            calcRelavanceOptionTwo()
        if (value == str(3)):
            printInterval()


def calOfRelevenceTriagle(a, m, b, x):
    if (x <= a):
        return 0
    elif (a < x <= m):
        return (x - a) / (m - a)
    elif (m < x <= b):
        return (b - a) / (b - m)
    else:
        return 0


def calOfRelevenceoftrapeze(a, m, n, b, x):
    if (x <= a):
        return 0
    elif (a < x <= m):
        return (x - a) / (m - a)
    elif (n < x <= m):
        return 1
    elif (m < x <= b):
        return (b - a) / (b - m)
    else:
        return 0


def calcByGroup(group, value):
    if group == "Baixo":
        return calOfRelevenceTriagle(1, 1, 1.5, value)
    if group == "Medio":
        return calOfRelevenceTriagle(1, 1.5, 2.0, value)
    if group == "Alto":
        return calOfRelevenceTriagle(1.65, 2.0, 2.0, value)
    else:
        print("Group not Found->" + group)


def calcRelevance(value):
    if isfloat(value):
        value = float(value)
        uBaixo = calOfRelevenceTriagle(1, 1, 1.5, value)
        uMedio = calOfRelevenceTriagle(1, 1.5, 2.0, value)
        uAlto = calOfRelevenceTriagle(1.65, 2.0, 2.0, value)
        print("Baixo:" + str(uBaixo) + " Medio: " + str(uMedio) + " Alto: " + str(uAlto))


def calcRelavanceOptionTwo():
    value = input("Type the interval: ")
    value1 = input("Type the interval: ")
    step = input("Type the step: ")
    group = input("Type the group: ")
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


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        print("Try a valid number Like 1 or 1.0")
        return False


# Imprima na tela o intervalo  correspondente ao suporte do conjunto escolhido

def printInterval():
    group = input("Type the group: ")
    if group == "Baixo":
        supportBaixo()
    if group == "Medio":
        supportMedio()
    if group == "Alto":
        supportAlto()
    else:
        print("Group not Found->" + group)


# Imprima na tela o intervalo correspondente ao núcleo do conjunto escolhido

def printCore():
    group = input("Type the group: ")
    if group == "Baixo":
        supportBaixo()
    if group == "Medio":
        supportMedio()
    if group == "Alto":
        supportAlto()
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
    trigInf = True
    while (count < 2):
        count = count + 0.00001
        x = calOfRelevenceTriagle(1, 1.5, 2.0, count)
        if (x >= 0.999):
            suportInf = count
            while (count < 2):
                x = calOfRelevenceTriagle(1, 1.5, 2.0, count)
                if (x < 0.999):
                    trigSup = count
                    break;
            break;

        print("[" + str(suportSup) + " , " + str(suportInf) + "]")


if __name__ == '__main__':
    main()
