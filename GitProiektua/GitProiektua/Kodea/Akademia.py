'''
Created on 9 mar. 2018

@author: DM3-1-05
'''

class Akademia:
    # Eraikitzailea
    def __init__(self, izena, helbidea, herria, pk, tlf, email, nif):
        self.izena = izena
        self.helbidea = helbidea
        self.herria = herria
        self.pk = pk
        self.tlf = tlf
        self.email = email
        self.nif = nif
    
    # Datuak bistaratzeko metodoa   
    def datuakBistaratu(self):
        print("AKADEMIAREN DATUAK: ")
        print("\tIzena: ", self.izena)
        print("\tHelbidea: ", self.helbidea)
        print("\tHerria: ", self.herria)
        print("\tPosta kodea: ", self.pk)
        print("\tTelefonoa: ", self.tlf)
        print("\tEmail-a: ", self.email)
        print("\tNIF-a: ", self.nif)
        
        print("testing branch-a aldatuta")
        print("Kaixoo, ni Eider naz.")