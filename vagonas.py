class Vagonas:
    def __init__(self,name, mase, maxMase,ID):
        self.name = name
        self.mase = mase
        self.maxMase = maxMase
        self.ID = ID
        self.maseKroviniu = 0
    


    def __str__(self):
        return "mase = %s, pavadinimas = %s, maksimali mase= %s \n" %(self.name, self.mase, self.maxMase)

    def addKrovinys(self, maseKrov):
        if  self.maxMase >= maseKrov + self.maseKroviniu:
            self.maseKroviniu += maseKrov
            print(self.maseKroviniu)
            return True
        return False

    def getVagName(self):
        return self.name
    
    def getVagMase(self):
        return self.mase
    
    def getVagMaxMase(self):
        return self.maxMase

    def getVagId(self):
        return self.ID

    def getVagMaseKroviniu(self):
        return self.maseKroviniu
    
    def setMasKrov(self, mase):
        self.maseKroviniu = mase
            
     
##        
##    def getIdVag(self, id):
##        return self.id
##
##    def getForeignId(self):
##        return self.foreign_key
    
##    
##    def getVagonai(self):
##        return "Vagonas: %s, mase = %s, maksimali mase = %s" %(self.name, self.mase, self.maxMase)

    #  def __str__(self):
   #     return self.name

    def __name__(self):
        return "Vagonas: %s" %(self.name)

    def getVagonasName(self):
        return self.name
    
    def getVagonasLaisvaMase(self):
        return self.maxMase - self.maseKroviniu

        
    def __unicode__(self):
        return self.name

    def __len__(self,):
        return self._len__

    def get_id(self):
        return id


