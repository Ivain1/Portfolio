class Sword:
    def __init__(self,Pommel,Hilt,Crossguard,Blade,Scabbard,Extra1):
        self.Pommel = Pommel

        self.Hilt = Hilt

        self.Crossguard = Crossguard

        self.Blade = Blade

        self.Scabbard = Scabbard

        self.D = 100 #Durability


    def Pommel(self,pomMat,pomGem,pomShape):
        pommelMaterials ={
            'Wood':'A pommel made out of wood'
            'Bronze': 'A pommel made out of weathered bronze'
            'Steel': 'A pommel made out of forged steel'
            'Silver': 'A pommel made out of purifying silver'
            'Gold': 'A pommel made out of glittering gold'
        }


    def Hilt(self,hiltMat,hiltLength):

    def Crossguard(self,guardType,guardMat,guardWidth,guardHeight,guardGem):
        crossguardMaterials = {
            'Wood': 'A crossguard made of wood'
            'Bronze': 'A crossguard made of weathered bronze'
            'Steel':'A crossguard made out of forged steel'
            'Silver': 'A crossguard made out of purifying silver'
            'Gold':'A crossguard made out of glittering gold'

        }

    def Blade(self,bladeShape,bladeLength,bladeTip,bladeSpecial):

    def Scabbard(self,scabType,scabMat,scabDeco):

    def Extra1(self,extraType):
