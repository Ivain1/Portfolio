#Note for this project: These weapons will be approximately modeled by Dark Souls style stats.

class straight_sword: #This is the object for a
    def __init__(self):
        self.w = 1 #Weight
        self.l = 1 #Length/Reach
        self.s = 1 #Speed of attack
        self.d = 100 #raw damage
        self.str = 1 #Strength scaling
        self.dex = 1 #Dexterity Scaling
        self.int = 1 #Intelligence Scaling (for magic)
        self.faith = 1 #Faith scaling, for divine
        self.m = 1 #final Damage multiplier
        self.d = 100 #durability
        self.e = 0 #enchantment. 0 = none, 1 = raw, 2 = fire, 3 = magic, 4 = divine
        self.u = 0 #Level upgrade. Goes from 0 to 10

    def multiplier(self, str, dex, int, faith):
        s = (str/100)
        d = (dex/100)
        i = (int/100)
        f = (faith/100)

        self.str = self.str + s
        self.dex = self.dex + d
        self.int = self.int + i
        self.faith = self.faith + f


        print(self.str,self.dex,self.int,self.faith)



    def upgrade(self):
        if self.e == 0:
            self.u = self.u + 1
        elif self.e == 1:
            self.int = self.int + 0.1
        print(self.u)



sword = straight_sword()
sword.multiplier(10,10,10,10)
sword.upgrade()