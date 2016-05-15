from lokomotyvas import Lokomotyvas
from vagonas import Vagonas

class Traukinys():
    def __init__(self,name,mase,tempGalia):

        self.lokomotyvas = Lokomotyvas(name, mase,tempGalia)
        self.vagonai = []
     
    def addTo(self, id):
        vagonai.append(id())

    def addVagonai(self, name, mase, maxMase):
        self.vagonai.append(Vagonas(name,mase,maxMase))

    def getVagonai(self):
        return self.vagonai
    
    def __sub__(a, b):
        return a-b
    
    def getLokomotyvas(self, vagonai):
        return self.lokomotyvas
        
   

##    def __repr__(self):
##       return "Vagonas: %s, mase = %s" %(self.name, self.mase, )

##    def __str__(self):
##        return self.name
    
   # def __unicode__(self):
    #    return self.name

    def __len__(self,):
        return self._len__

    def get_id(self):
        return id
    
a = Traukinys("vardas",30,40)
##print(a.getLokomotyvas)
a.addVagonai("vagons1",40,30)
##import pdb; pdb.set_trace()
a.addVagonai("vagons_2",50,30)


print(a.getLokomotyvas(777))
print(a.getVagonai())
##a.addVagonai("vagonas",20,30)
##a.addVagonai("vagonas_2",15,20)
##
##
##print (a.getVagonai)
##print(a.getVagonai)
##b = Traukinys(id)
##b = Traukinys("vardas",3)
##b.create
####a.priskirt(4)
##print (b)

