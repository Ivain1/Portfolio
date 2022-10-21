#This is the file for various types of entities
from random import randint

class skeleton():
    def __init__(self):
        self.hp = 10
        self.ep = 10
        self.right = []
        self.left = []
        self.head = []
        self.chest = []
        self.arms = []
        self.legs = []
        self.rings = []

    def equip(self, points):
        weapons = ['dagger','club', 'shortsword', 'scimitar', 'longsword', 'bow', 'spear']
        shields = ['none', 'small wooden shield', 'metal buckler', 'round leather shield', 'knight shield']
        head = ['none', 'leather cap', 'rusted iron cap']
        chest = ['none', 'padded shirt', 'tattered chainmail', 'rusty iron breastplate']
        arms = ['none', 'leather bracers', 'chainmail gloves', 'iron gloves']
        legs = ['none', 'tattered waistband', '']


