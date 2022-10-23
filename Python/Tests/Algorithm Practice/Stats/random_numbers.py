from random import randint, choice
import matplotlib.pyplot as plt
from numpy import array
import numpy as np

def generate(amount,mini=0,maxi=10):
    number_list = []
    for i in range(0,amount):
        number = randint(mini,maxi)
        number_list.append(number)
        #print(number_list)
    return(number_list)

def dataset_generate(central,deviation,amount):
    return (np.random.normal(central, deviation, amount))
    #return(np.round(np.random.normal(central,deviation,amount)))

def histogram(dataset):
    print('Histogram has been plotted')
    return(plt.hist(dataset,100))


def sort(data,ascend=True):
    return sort(data)

def frequency_count(data,maxi=10):
    freq = []
    for i in range(0,maxi):
        freq.insert(i,0)
        base_freq = freq.pop(i)
        number_freq = data.count(i) + base_freq
        freq.insert(i,number_freq)
        #print('The number {0} occurs {1} times in this collection'.format(i,number_freq))
    return(freq)

def bar_plot(data, mini=0, maxi=10):
    categories = []
    for i in range(mini,maxi):
        categories.append(i)
    x = array(categories)
    y = array(data)
    return(plt.bar(x,y, width=1,color=('red','orange','yellow','green','cyan','blue','purple','magenta','pink')))

def random_bool(amount,integer = False):
    choices =[]
    if integer == False:
        for i in range(0,amount):
            choices.append(choice([True,False]))
    else:
        for i in range(0,amount):
            choices.append(randint(-1,1))
    return(choices)

def array_add(original, addition):
    return(np.add(original,addition))


minimum = 0
maximum = 10
amount = 10000
data = generate(amount,minimum,maximum)
#print(data)
#frequency_count(data,maximum)
#bargraph = bar_plot(frequency_count(data, maximum), minimum, maximum)
data = dataset_generate(50,10,amount)
for i in range(0,amount):
    addition = random_bool(amount, True)
    data = array_add(data,addition)
    #print(data)
histo = histogram(data)

plt.show()
