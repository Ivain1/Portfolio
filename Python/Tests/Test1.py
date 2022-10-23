'''inputName = str(input('Uw naam hier, alstublieft: '))

def userGreet(userName): #Geeft de gebruiker een persoonlijke begroeting gebaseerd op: -Naam


    secretUser = str('Batman')
    if userName == secretUser:
        print('Initializing BatCave Security Protocols...\nSecuring Digital Environment...\nCapturing Rogues...\nSummoning Alfred...\nWelcome Back, Batman!')
    else:
        print('Welkom terug, Gebruiker', userName, '\nHet Systeem is klaar voor gebruik\nGeen veranderingen sinds de vorige keer dat u ingelogd heeft')


print(dir())'''
from random import randint
test1 = randint(-2,10)
typeList = ['bool','int','float','string','tuple','list','dict']

def Converter(testValue,valueType = str("int")):
    #converterList = {'bool':bool(testValue),'int':int(testValue),'float':float(testValue),'string':str(testValue),'tuple':tuple(testValue),'list':list(testValue),'dict':dict(testValue)}
    print(valueType)
    inputValue = str(type(testValue))
    excess, splitter, inputValue = inputValue.partition(" ")
    inputValue = list(inputValue)
    print(inputValue)
    valueLength = len(inputValue)
    excessIndexer = inputValue.index('>')
    inputValue.pop(excessIndexer)
    excessIndexer = inputValue.index("'")
    inputValue.pop(excessIndexer)
    excessIndexer = inputValue.index("'")
    inputValue.pop(excessIndexer)
    inputValue = ''.join(inputValue)
    if inputValue == valueType:
        print('The input value already matches the desired type')
    else:
        if valueType == typeList.index(valueType):
        #print(inputMatch)
        #if inputMatch == true :
            print('The desired type conversion is available.\nAttempting to oonvert now...')
            #converterList.pop(valueType)
            #conversionIndex = typeList.index(valueType)
            #print(conversionIndex)
            #converterFunction = converterList.pop(conversionIndex)
            #print(converterFunction)

        else:
            print('The desired type input is invalid. Available types are:' ,typeList)



    #print(inputValue)
    #inputValue = ' '.join(inputValue)
    print(inputValue)
    print(valueType)

Converter(test1,'nonsense')
