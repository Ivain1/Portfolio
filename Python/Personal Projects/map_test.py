from random import randint

def random_list_fill(length,reach):
    newlist = []
    for i in range(0,length):
        number = randint(0,reach)
        newlist.append(number)
    return(newlist)


list1 = random_list_fill(10,10)
list2 = random_list_fill(10,10)

def list_add(list_1, list_2):
    '''Add 2 list values together to get a third list'''
    result = map(lambda x, y: x + y, list_1, list_2)
    return(list(result))
list3 = list_add(list1,list2)
list4 = [list1,list2,list3]

def list_average(big_list, rounded = False):
    '''Input a list of multiple lists to get a new list that has the average values
        <big_list> is the list containing the lists to be added
    '''
    list_count = len(big_list)
    print(list_count)
    total = sum(map(sum,big_list))
    if rounded == True:
        return(int(total/list_count))
    else:
        return(total/list_count)

print(list_average(list4,True))
test1 = 0



class block:
    def __init__(self,x,y,height,mat):
        if type(x) == int and type(y) == int:
            try:
                if type(height) == int:
                    try:
                        if type(mat) == str:
                            try:
                                self.x = x
                                self.y = y
                                self.h = height
                                self.m = mat
                            except ValueError:
                                print('{0} is not a valid input for a material'.format(mat))
                    except ValueError:
                        print('{0} is not a valid input for the height'.format(height))
            except ValueError:
                print('{0},{1} is not a valid input for the coordinates'.format(x,y))

    def output(self):
        print('This block is located at {0},{1}, is {2} blocks high, and is made of material {3}'.format(self.x,self.y,self.h,self.m))
        
    def height_raise(self,increase):
        if type(increase) == int:
            try:
                self.h = self.h + increase
            except ValueError:
                print('The input is not an integer')

    def above_height(self, height):
        return(self.h > height)

    def below_height(self,height):
        return(self.h < height)

    def exact_height(self, height):
        return(self.h == height)

    def material_change(self,material):
        self.m = material

    def check_material(self,material):
        return(self.m == material)

    def shift_coords(self,x,y):
        self.x = self.x + x
        self.y = self.y + y

stone = block(10,10,100,'stone')

print(stone.output())
print(stone.above_height(99))
array = []
for x in range(0,16):
    for y in range(0,16):
        list1 = block()

class chunk:
    def __init__(self,x_pos = 0,y_pos = 0,avg_height = 60,biome = 'plains',blocks = [],max_height = 255):
        self.x = x_pos
        self.y = y_pos
        self.h = avg_height
        self.b = biome
        self.bl = blocks
        self.max = max_height

    def array_setup(self):
        block_list = self.bl
        #for i in range(0,self.max):







