class Poste(object):
    
    def __init__(self,dest,exp,poids,mode):
        self._dest=dest
        self._exp=exp
        self._poids=poids
        self._mode=mode
        self._prix=0
        
    def calculTimbre(self):
        pass
    
    def ToString(self):
        self.calculTimbre()
        print("Adresse destination:",self._dest)
        print("Adresse expedition:",self._exp) 
        print("Poids:",str(self._poids),"grammes")
        print("Mode:",self._mode)

class Lettre(Poste):
    
    def __init__(self,dest,exp,poids,mode,forma):
         super().__init__(dest,exp,poids,mode)
         self._format=forma
    
    def calculTimbre(self):
        timbre = 0
        if(self._format=="A4"):
            timbre = 2.50
        elif(self._format=="A3"):
            timbre = 3.50
        self._prix = timbre + self._poids/1000.00
        if(self._mode == "expresse"):
            self._prix*=2

    def ToString(self):
        super().ToString()
        print("Format:",self._format)
        print("Prix du timbre:",str(self._prix))

class Collis(Poste):
    
    def __init__(self,dest,exp,poids,mode,volume):
         super().__init__(dest,exp,poids,mode)
         self._volume=volume
    
    def calculTimbre(self):
        self._prix = 0.25*self._volume * (self._poids/1000.00)
        if(self._mode == "expresse"):
            self._prix*=2
    
    def ToString(self):
        super().ToString()
        print("Volume:",str(self._volume),"litres")
        print("Prix du timbre:",str(self._prix))