
import numpy as np

enter =0
def main():
    print(" Welcome! \n  The Fuzzy Program\n")
    while (1):
        print(" Choose one option bellow:")
        print("1- Calc one Relevance:")
        print("2- Calc interval Of Relance:")
        print("3- Print interval of suport by group:")
        print("4- Print interval of core by group:")
        print("5- Print interval of alfa cut:")
        value = input()
        if (value == str(1)):
            value = input('The height:')
            func = input('Function:')
            if func == 1:
                calcRelevance(value)
            else:
                calcRelevance(value)

        if (value == str(2)):
            func = input('Function:')
            if func == 1:
                calcRelavanceOptionTwo(func)
            else:
                calcRelavanceOptionTwo(func)
        if (value == str(3)):
        	 func = input('Function:')
        	 enter = func
        	 printInterval()
        if (value == str(4)):
             group = input('group:')
             coreBaixo(group )
        if (value == str(5)):
            group = input('group:')
            alfa = input ('Alfa :')
            alfaCorte(float(alfa),group)

def calOfRelevenceTriagle(a, m, b, x):
    if (x <= a):
        return 0
    elif (a < x <= m):
        return (x - a) / (m - a)
    elif (m < x <= b):
        return (b - x) / (b - m)
    else:
        return 0


def calOfRelevenceoftrapeze(a, m, n, b, x):
    if (x <= a):
        return 0
    elif (a < x <= m):
        return (x - a) / (m - a)
    elif (n < x <= n):
        return 1
    elif (n < x <= b):
        return (b - x) / (b - n)
    else:
        return 0


def calcByGroup(group, value,func):
    if func==1:
        if group == "Baixo":
            return calOfRelevenceTriagle(1, 1, 1.5, value)
        elif group == "Medio":
            return calOfRelevenceTriagle(1, 1.5, 2.0, value)
        elif group == "Alto":
            return calOfRelevenceTriagle(1.65, 2.0, 2.0, value)
        else:
            print("Group not Found->" + group)
    else:
        if group == "Baixo":
            return calOfRelevenceoftrapeze(1, 1, 0.7, 1.5, value)
        elif group == "Medio":
            return calOfRelevenceoftrapeze(1, 1.4, 1.6,2.0, value)
        elif group == "Alto":
            return calOfRelevenceoftrapeze(1.5, 1.8, 2.0,2.0, value)
        else:
            print("Group not Found->" + group)


def calcRelevance(value):
    if isfloat(value):
        value = float(value)
        uBaixo = calOfRelevenceTriagle(1, 1, 1.5, value)
        uMedio = calOfRelevenceTriagle(1, 1.5, 2.0, value)
        uAlto = calOfRelevenceTriagle(1.65, 2.0, 2.0, value)
        print("Baixo:" + str(uBaixo) + " Medio: " + str(uMedio) + " Alto: " + str(uAlto))


def calcRelevanceTra(value):
    if isfloat(value):
        value = float(value)
        uBaixo = calOfRelevenceoftrapeze(1, 1, 0.7, 1.5, value)
        uMedio = calOfRelevenceoftrapeze(1, 1.4, 1.6,2.0, value)
        uAlto = calOfRelevenceoftrapeze(1.5, 1.8, 2.0,2.0, value)
        print("Baixo:" + str(uBaixo) + " Medio: " + str(uMedio) + " Alto: " + str(uAlto))



def calcRelavanceOptionTwo(func):
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
            results.append(calcByGroup(group, array[x],func))

        twodecimals = ["%.2f".strip("\'") % v for v in results]
        print(array)
        print(twodecimals)


def calcRelavanceOptionTwoTra():
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
    group = input("Type the group: ")
    if group == "Baixo":
	 	 	print("[1 , 1.5)") 	      
    if group == "Medio":
       		 print("(1 , 2.0)") 
    if group == "Alto":
        if  enter== 1:
        	print("(1.65 , 2.0)")
        else:
        	print("(1.5 , 2.0)") 
    else:
        print("Group not Found->" + group)

 #Imprima na tela o intervalo correspondente ao ncleo do conjunto escolhido

def printCore():
    group = input("Type the group: ")
    if group == "Baixo":
        coreBaixo()
    if group == "Medio":
        coreMedio()
    if group == "Alto":
        coreAlto()
    else:
        print("Group not Found->" + group)



def coreBaixo(group, func):
    count = 1
    suportInf = 0
    suportSup = 0
    trigSup = True
    trigInf = False
    while (count < 2):
        count = count + 0.0001
        x = calcByGroup(group, count, func)
        if (0.99999 < x <= 1):
            suportInf = count
            while (count < 2):
                count = count + 0.0001
                x = calcByGroup(group, count, func)
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



def alfaCorte(alfa, group):

    count = 1
    suportInf = 0
    suportSup = 0
    trigSup = True
    trigInf = False
    while (count < 2):
        count = count + 0.0001
        x = calcByGroup(group, count, func)
        if (x>= alfa):
            suportInf = count
            while (count < 2):
                count = count + 0.0001
                x = calcByGroup(group, count, func)
                if (x>= alfa):
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
