from sensor import MonederoSensor

class cafeteraBasica(object):

    def __init__(self):
        self.monedero = MonederoSensor()
        self.haciendoCafe = False
        self.agua = 1000
        self.cafe = 100
        self.azucar = 100
        self.moneda = 0

    def cafetera(self, moni):
        self.moneda = moni
        if self.moneda == 1:
            if self.agua == 0:
                return 'No hay agua'
            if self.cafe == 0:
                return 'No hay cafe'
            if self.azucar == 0:
                return 'No hay azucar'
            else:
                self.haciendoCafe = True
                self.moneda -= 1
                return 'Haciendo cafe'

    def aguaCant(self, aguaML):
        if self.haciendoCafe == True:
            if int(aguaML) > self.agua:
                self.haciendoCafe = False
                return 'No hay agua suficiente'
            else:
                self.agua -= int(aguaML)
                return 'Con ' + str(aguaML) + 'ml de agua' 

    def cafeCant(self, cafeG):
        if self.haciendoCafe == True:
            if cafeG > self.cafe:
                self.haciendoCafe = False
                return 'No hay cafe suficiente'
            else:
                self.cafe -= cafeG
                return 'Con ' + str(cafeG) + 'g de cafe'

    def azucarCant(self, azucarG):
        if self.haciendoCafe == True:
            if azucarG > self.azucar:
                self.haciendoCafe = False
                return 'No hay azucar suficiente'
            if azucarG == 0:
                return 'Sin azucar'
            else:
                self.azucar -= azucarG
                return 'Con ' + str(azucarG) + 'g de azucar'  

class cafeteraPremium(cafeteraBasica):
    def __init__(self):
        self.haciendoCafeP = False
        self.aguaP = 1000
        self.cafeP = 100
        self.azucarP = 100
        self.monedaP = 0
    
    def vasoSN(self, vasoOP, moniP):
        self.moneda = moniP
        if self.moneda == 1 and vasoOP == True:
            if self.aguaP == 0:
                return 'No hay agua'
            if self.cafeP == 0:
                return 'No hay cafe'
            if self.azucarP == 0:
                return 'No hay azucar'
            else:
                self.haciendoCafeP = True
                self.monedaP -= 1
                return 'Haciendo cafe'
        if vasoOP == False:
            self.haciendoCafeP == False
            return 'Ponga un vaso'

    def aguaCantP(self, aguaMLP):
        if self.haciendoCafeP == True:
            if int(aguaMLP) > self.aguaP:
                self.haciendoCafeP = False
                return 'No hay agua suficiente'
            else:
                self.aguaP -= int(aguaMLP)
                return 'Con ' + str(aguaMLP) + 'ml de agua'

    def cafeCantP(self, cafeGP):
        if self.haciendoCafeP == True:
            if cafeGP > self.cafeP:
                self.haciendoCafeP = False
                return 'No hay cafe suficiente'
            else:
                self.cafeP -= cafeGP
                return 'Con ' + str(cafeGP) + 'g de cafe'

    def azucarCantP(self, azucarGP):
        if self.haciendoCafeP == True:
            if azucarGP > self.azucarP:
                self.haciendoCafeP = False
                return 'No hay azucar suficiente'
            if azucarGP == 0:
                return 'Sin azucar'
            else:
                self.azucarP -= azucarGP
                return 'Con ' + str(azucarGP) + 'g de azucar'  

    def lecheCant(self, lecheSN):
        if self.haciendoCafeP == True:
            if lecheSN == True:
                return 'Con leche'
            if lecheSN == False:
                return 'Sin leche'