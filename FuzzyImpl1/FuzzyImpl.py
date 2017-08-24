
import numpy as np

def main():

    print(" Welcome! \n  The Fuzzy Program\n")
    while(1):
        print(" Choose one option bellow:")
        value = input("1- Calc one Relevance:\n"
                      "2- Calc interval Of Relance:")
        if(value == str(1)):
            value = input('The higher:')
            calcRelevance(value)
        if(value == str(2)):
            calcRelavanceOptionTwo()
            


def calOfRelevenceTriagle(a , m ,b , x):

    if(x<=a):
        return 0
    elif(a<x<=m):
        return (x-a)/(m-a)
    elif(m<x<=b):
        return (b-a)/(b-m)
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

def  calcByGroup(group, value):

    if group == "Baixo" :
        return calOfRelevenceTriagle(1,1,1.5,value)
    if group == "Medio":
        return calOfRelevenceTriagle(1,1.5,2.0, value)
    if group == "Alto":
        return calOfRelevenceTriagle(1.65,2.0,2.0, value)
    else:
        print("Group not Found->"+ group)

def  calcRelevance(value):

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

if  __name__ =='__main__':
    main()

