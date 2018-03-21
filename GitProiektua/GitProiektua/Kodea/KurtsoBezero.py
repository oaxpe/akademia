'''
Created on 7 mar. 2018

@author: DM3-1-05
'''


class KurtsoBezero:
    # Eraikitzailea
    def __init__(self, matrikulaData, prezioa):
        self.matrikulaData = matrikulaData
        self.prezioa = prezioa

     
    # Datuak bistaratzeko metodoa   
    def datuakBistaratu(self):
        print("\tMatrikula data: ", self.matrikulaData)
        print("\tPrezioa: ", self.prezioa)
