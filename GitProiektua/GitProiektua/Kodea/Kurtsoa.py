'''
Created on 7 mar. 2018

@author: DM3-1-05
'''


class Kurtsoa:
    # Eraikitzailea
    def __init__(self, kodea, izena, plazaKopMax, orduKop, iraupena, prezioa, ikasleKop):
        self.kodea = kodea
        self.izena = izena
        self.plazaKopMax = plazaKopMax
        self.orduKop = orduKop
        self.iraupena = iraupena
        self.prezioa = prezioa
        self.ikasleKop = ikasleKop
     
    # Datuak bistaratzeko metodoa   
    def datuakBistaratu(self):
        print("KURTSOAREN DATUAK: ")
        print("\tKodea: ", self.kodea)
        print("\tIzena: ", self.izena)
        print("\tPlaza kopuru maximoa: ", self.plazaKopMax)
        print("\tOrdu kopurua: ", self.orduKop)
        print("\tIraupena: ", self.iraupena)
        print("\tPrezioa: ", self.prezioa)
        print("\tIkasle Kopurua: ", self.ikasleKop)
    
    # Irabaziak kalkulatzeko metodoa   
    def Irabaziak(self):
        print("Kurtsoaren irabaziak: ")
        return (self.prezioa*self.ikasleKop)
    
k1 = Kurtsoa("INF001", "Informatika", 23, 40, "3 hilabete", 50.65, 6)
k2 = Kurtsoa("A", "Informatika", 23, 40, "3 hilabete", 1, 6)
print(k1.__dict__) # datuak ikusteko
print(k1.Irabaziak())
print(k2.Irabaziak())
