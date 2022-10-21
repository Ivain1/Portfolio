from random import randint
import statistics

data = []
for i in range(0,10):
    num = randint(0,100)
    data.append(num)
print(data)



def myRound(number,round='NEAR'):
    '''

    :param number: float
    :param round: 'UP', 'DOWN' and 'NEAR'
    :return: float
    '''
    decimal = number % 1
    if round == 'UP':
        decimal = 1-decimal
        number = number + decimal
    elif round == 'DOWN':
        number = int(number-decimal)
    elif round == 'NEAR':
        if decimal >= 0.5:
            decimal = 1-decimal
            number = number + decimal
        else:
            number = number - decimal
    else:
        print('invalid')
        return('ERROR: invalid input, choose UP, DOWN or NEAR')

    return(number)

def myMean(dataset=[],round=True):
    '''
    :param dataset is a list:
    :return is a floating point number:
    '''
    length = len(dataset)
    number = 0
    for i in range(0,length):
        number = number + dataset[i]
    result = number/length

    if round==True:
        result = myRound(result)
    else:
        pass
    return(result)


def myMedian(dataset=[]):
    dataset.sort()
    length = len(dataset)
    med1 = int(myRound(length/2,'UP'))
    med2 = int(myRound(length/2,'DOWN'))
    print(med1,med2)
    num1 = dataset[med1]
    print(num1)
    num2 = dataset[med2]
    print(num2)
    number = (num1 + num2)/2
    print(number)
    return(number)
    #number = dataset[med]
    #return(number)



num1 = myMean(data, False)
num2 = myMedian(data)
num3 = statistics.mean(data)
num4 = statistics.median(data)

print('The mean of the dataset is {0}, the median of the dataset is {1}, the statistics mean is {2}, the statistics median is {3}'.format(num1,num2,num,num4))
