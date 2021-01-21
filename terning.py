import random
import sys

print("Velkommen til terningeprogrammet, hvor du selv bestemmer antallet af terninger og øjne på disse.")
print("*** Udviklet af Mathias Rõzko Tryggedsson ***")
abort = "Du kan afbryde programmet ved at trykke 'x'."
print(abort)
def CheckType(diceNum):
    try:
        diceNum = int(diceNum)
        return True
    except ValueError:
        print(properInput)
    diceType = isinstance(diceNum, int)
    if(diceType == False):
        return False
    else:
        return True

def CheckValue(value):
    if(value <1):
        print(properValue)
        return False
    else:
        valueOk = True
        return True

def Convert(value):
    value = int(value)
    return value

def ThrowDice(diceNum, diceVal):
    i = 1
    while i <= diceNum:
        dice = random.randint(1,diceVal)
        print("Terning #"+str(i)+" slog "+str(dice)+".")
        i += 1
    print("\n")

def Terminate():
    sys.exit()

diceNum = 0
properInput = "Venligst indtast antallet som et heltal med cifre!"
properValue = "Venligst indtast en værdi større end 0!"
goodbye = "Farvel og tak for denne gang!"

while(diceNum != 'x'):
    diceType = False
    valueOk = False
    while(diceNum != 'x' and valueOk != True):
        diceNum = input("Indtast antallet af terninger:\n>")
        if(diceNum.lower().strip() == 'x'):
            print(goodbye)
            Terminate()
            break
        if(CheckType(diceNum) == True):
            diceNum = Convert(diceNum)
            valueOk = CheckValue(diceNum)
        if(valueOk == True):
            break
    print("Du har valgt "+str(diceNum)+" terninger.")

    diceVal = 0
    valueOk = False
    while(diceVal != 'x' and valueOk != True):
        diceVal = input("Indtast antallet af sider på terningen:\n>")
        if(diceVal.lower().strip() == 'x'):
            print(goodbye)
            Terminate()
            break
        if(CheckType(diceVal) == True):
           diceVal = Convert(diceVal)
           valueOk = CheckValue(diceVal)
        if(valueOk == True):
            break
    print("Du har valgt "+str(diceVal)+" sider på hver terning.")
    diceVal = Convert(diceVal)
    diceNum = Convert(diceNum)
    print("Terningerne kastes...")
    ThrowDice(diceNum, diceVal)



    