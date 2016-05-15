from lokomotyvas import Lokomotyvas
from vagonas import Vagonas

class Traukinys():
    def __init__(self):

        self.lokomotyvai = []
        self.vagonai = []
        self.bendraKroviniuMase = 0
        self.galiaTrauk = 0
        self.bendraMase = 0
    
    def addLokomotyvas (self, name, mase, tempGalia):
        self.lokomotyvai.append(Lokomotyvas(name, mase,tempGalia))
        self.galiaTrauk += tempGalia
        self.bendraMase += mase
        
    def addVagonas(self, name, mase, maxMase):
        self.vagonai.append(Vagonas(name,mase,maxMase))
        self.bendraMase += mase
        
    def getGaliaTrauk(self):
        return print("traukinio bendroji tempemoji galia : %s" %(self.galiaTrauk))
    
    def galiaTrauk(self):
        return self.galiaTrauk

    def getVagonas(self):
        return self.vagonai

    def pakrautiKrovini(self, masKrov):
        if self.galiaTrauk < self.bendraMase + masKrov:
            return print("virsyta mase, kuria gali tempti traukinys-----prideti nepavyko")
        else:
            for vagonas in self.vagonai:
                a = vagonas.addKrovinys(masKrov)
                if a == False:
                    continue
                else:
                    self.bendraMase += masKrov
                    if vagonas.getVagonasLaisvaMase() == 0:
                        return print("Pavyko prideti, vagonas %s jau pilnas" %(vagonas.getVagonasName()))
                    else:
                        return print("pavyko prideti krovini i %s dar liko %s vietos siame vagone  "%(vagonas.getVagonasName(),
                                                                                   vagonas.getVagonasLaisvaMase()))
            return print("nepavyko prideti, reikia didesniu vagonu")
 
            
             
            
    
    def __sub__(a, b):
        return a-b
    
    def getLokomotyvas(self):
        return self.lokomotyvai
        
   

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
    
a = Traukinys()
a.addLokomotyvas("lokomotyvas",100,500)
a.addLokomotyvas("juzesLoko", 80,300)
a.addLokomotyvas("lokomotyvas",100,500)
##print(a.getLokomotyvas)
a.addVagonas("vagons1",40,500)
##import pdb; pdb.set_trace()
a.addVagonas("vagons_2",50,300)
a.addVagonas("rimtas",50,500)
a.pakrautiKrovini(500)
a.pakrautiKrovini(100)
a.pakrautiKrovini(200)
print (a.bendraMase)

