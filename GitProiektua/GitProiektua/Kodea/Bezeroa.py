'''
Created on 14 mar. 2018

@author: DM3-1-05
'''
class Bezeroa:
    # Eraikitzailea
    def __init__(self, nan, izena, abizena, helbidea, tlf, email, kk):
        self.nan = nan
        self.izena = izena
        self.abizena = abizena
        self.helbidea = helbidea
        self.tlf = tlf
        self.email = email        
        self.kk = kk
    
    # Datuak bistaratzeko metodoa   
    def datuakBistaratu(self):
        print("BEZEROAREN DATUAK: ")
        print("\tNAN zenbakia: ", self.nan)
        print("\tIzena: ", self.izena)
        print("\tAbizena: ", self.abizena)
        print("\tHelbidea: ", self.helbidea)
        print("\tTelefonoa: ", self.tlf)
        print("\tEmail-a: ", self.email)
        print("\tKontu korronte zenbakia: ", self.kk)