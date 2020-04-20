class DateNaissance(object):
    
    def __init__(self,day,month,year):
        self._day=day
        self._month=month
        self._year=year
    
    def _get_day(self):
        return self._day
    
    def _get_month(self):
        return self._month
    
    def _get_year(self):
        return self._year
    
    def toString(self):
        val = str(self._day)+"/"+str(self._month)+"/"+str(self._year)
        return val
    
class Personne(object):
    
    def __init__(self,nom,prenom,DateNaissance):
        self._nom=nom
        self._prenom=prenom
        self._dateNaissance=DateNaissance
   
    def afficher(self):
        print("Nom:",self._nom)
        print("Prénom:",self._prenom)
        print("Date de naissance:", self._dateNaissance.toString())

class Employe(Personne):
    
    def __init__(self,nom,prenom,DateNaissance,salaire):
        super().__init__(nom,prenom,DateNaissance)
        self._salaire = salaire
        
    def afficher(self):
        super().afficher()
        print("Salaire:",str(self._salaire))

class Chef(Employe):
    
    def __init__(self,nom,prenom,DateNaissance,salaire,service):
        super().__init__(nom,prenom,DateNaissance,salaire)
        self._service = service
        
    def afficher(self):
        super().afficher()
        print("Service:",self._service)