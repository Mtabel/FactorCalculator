
#Factoring Calculator - Matthew Tabel Jr.

'''
Matthew Tabel Jr.
Date 2/29/2024
4:14 PM
This Is a working Factoring Calculator that takes in 3 inputs Ax^2 + Bx + C >>> A B C in

No External Turotials Used
'''
def PositiveUpper_PositiveLower(mutiplyTo, b):
    foundValue = False
    x = 0
    y = 0
    z = abs(mutiplyTo)
    factorList = []
    adjacentValue = []
    for i in range(z):
        if(i != 0 and (z / i).is_integer()):
            factorList.append(i)
            adjacentValue.append(z / i)
    print(factorList)
    print(adjacentValue)
    
    for i in range(len(factorList)):
        if factorList[i] + adjacentValue[i] == b and factorList[i]  *  adjacentValue[i] == multiplyTo:
            foundValue = True
            x = int(factorList[i])
            y = int(adjacentValue[i])
            print("X: " + str(x) + "Y: " + str(y))
            break
    if not foundValue:
        print("There are no factors for this")       
            
    

def NegativeUpper_PositiveLower(mutiplyTo, b): 
    foundValue = False
    x = 0
    y = 0
    z = abs(mutiplyTo)
    factorList = []
    adjacentValue = []
    for i in range(z):
        if(i != 0 and (z / i).is_integer()):
            factorList.append(i)
            adjacentValue.append(z / i)
    print(factorList)
    print(adjacentValue)
    
    for i in range(len(factorList)):
        if -factorList[i] + adjacentValue[i] == b:
            foundValue = True
            x = int(-factorList[i])
            y = int(adjacentValue[i])
            print("X: " + str(x) + "Y: " + str(y))
            break
    if not foundValue:
        print("There are no factors for this") 
            
    
def NegativeUpper_NegativeLower(acValue, b):  
    foundValue = False
    x = 0
    y = 0
    z = abs(acValue)
    factorList = []
    adjacentValue = []
    for i in range(z):
        if(i != 0 and (z / i).is_integer()):
            factorList.append(i)
            adjacentValue.append(z / i)
    print(factorList)
    print(adjacentValue)
    
    for i in range(len(factorList)):
        if -factorList[i] + adjacentValue[i] == b and -factorList[i]  *  adjacentValue[i] == multiplyTo:
            foundValue = True
            x = int(-factorList[i])
            y = int(adjacentValue[i])
            print("X: " + str(x) + "Y: " + str(y))
            break
    if not foundValue:
        print("There are no factors for this")        
    

def PositiveUpper_NegativeLower(mutiplyTo, b): #+ -
    foundValue = False
    x = 0
    y = 0
    z = mutiplyTo
    factorList = []
    adjacentValue = []
    for i in range(z):
        if(i != 0 and (z / i).is_integer()):
            factorList.append(i)
            adjacentValue.append(z / i)
    print(factorList)
    print(adjacentValue)
    
    for i in range(len(factorList)):
        if -factorList[i] - adjacentValue[i] == b and -factorList[i]  * - adjacentValue[i] == multiplyTo:
            foundValue = True
            x = int(-factorList[i])
            y = int(-adjacentValue[i])
            print("X: " + str(x) + "Y: " + str(y))
            break
    if not foundValue:
        print("There are no factors for this")
   

print("Running")
recure = True

while recure:
    
    a = int(input('A value: '))
    b = int(input('B value: '))
    c = int(input('C value: '))

    multiplyTo = a*c
    if multiplyTo > 0:
        if b > 0:
            PositiveUpper_PositiveLower(multiplyTo, b)
            #print("WIP")
        else:
            PositiveUpper_NegativeLower(multiplyTo, b)
    elif multiplyTo < 0:
        if b >= 0:
            NegativeUpper_PositiveLower(multiplyTo, b)
        else:
            NegativeUpper_NegativeLower(multiplyTo, b)  
    elif multiplyTo == 0:
        print("A * C cannot equal 0!")

