class Banque(object):
    
    def __init__(self,nom,solde=1000):
        self._nom=nom
        self._solde=solde
    
    def depot(self,solde):
        self._solde+=solde
    
    def retrait(self,solde):
        self._solde-=solde
    
    def affiche(self):
        print("Le solde du compte bancaire de",self._nom,"est de",self._solde,"euros.")
    
    