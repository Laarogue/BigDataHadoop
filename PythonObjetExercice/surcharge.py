class Point(object):
    
    def __init__(self,X=0,Y=0,Z=0):
        self._X=X
        self._Y=Y
        self._Z=Z
    
    def toString(self):
        P=[self._X,self._Y]
        if(self._Z !=0):
            P = P + [self._Z]
        return P