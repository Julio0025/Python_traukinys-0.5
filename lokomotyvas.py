class Lokomotyvas:
    def __init__(self,name, mase,tempGalia):
        self.name = name
        self.mase = mase
        self.tempGalia = tempGalia
    def __sub__(a, b):
        return a-b

    def getLokName(self):
        return self.name
    
    def getLokMase(self):
        return self.mase
    
    def getLokGalia(self):
        return self.tempGalia
    
    def __repr__(self):
        return "%s" %(self.name)
    
    def __str__(self):
        return "Lokomotyvas = %s  Mase = %s, tempiamoji galia = %s "%(self.name, self.mase,self.tempGalia)

