
class Files():
    def __init__(self,name,path,data):
        self.name = str(name)
        self.path = path
        self.data = data

    def Open(self):
        File1 = open(self.name, 'a+')

    def Save(self):
        pass

