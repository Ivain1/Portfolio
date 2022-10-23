

class Sword:
    def __init__(self):
        self.b = 0 #blade id
        self.c = 0 #crossguard id
        self.h = 0 #hilt id
        self.du = 100
        self.da = 1
        self.broken = False

    def construct(self,blade,crossguard,hilt):
        self.b = blade
        self.c = crossguard
        self.h = hilt
        print('Constructed a new sword!')

    def hit(self, multiplier=1):
        if self.du > 0:
            self.du = int(self.du - 1)
            return(int(self.da*multipler))
        else:
            self.broken = True


