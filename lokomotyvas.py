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

    
##    def getLokomotyvas(self):
##        return 
    
    def __repr__(self):
        return "Lokomotyvas = %s  Mase = %s, tempiamoji galia = %s \n"%(self.name, self.mase,self.tempGalia)

  #  def __str__(self):
  #      return self.name
##    
##    def __unicode__(self):
##        return self.name
##
##    def __len__(self,):
##        return self._len__
##
##
