from lokomotyvas import Lokomotyvas
from vagonas import Vagonas
import json

class Traukinys():
    def __init__(self,name):
        self.nameTraukinys = name
        self.lokomotyvai = []
        self.vagonai = []
        self.bendraKroviniuMase = 0
        self.galiaTrauk = 0
        self.bendraMase = 0
    
    def addLokomotyvas (self, name, mase, tempGalia):
        if tempGalia >= mase:
            self.lokomotyvai.append(Lokomotyvas(name, mase,tempGalia))
            self.galiaTrauk += tempGalia
            self.bendraMase += mase
        else:
            return print("lokomotyvo tempiamoji galia negali buti mazesne uz jo mase")
        
    def addVagonas(self, name, mase, maxMase):
        if self.galiaTrauk < self.bendraMase + mase:
            return print("virsyta mase, kuria gali tempti dabartiniai lokomotyvai")
        else:
            self.vagonai.append(Vagonas(name,mase,maxMase))
            self.bendraMase += mase
        
    def getGaliaTrauk(self):
        return print("traukinio bendroji tempemoji galia : %s" %(self.galiaTrauk))
    
    def galiaTrauk(self):
        return self.galiaTrauk

    def getVagonas(self):
        return self.vagonai

    def getTrainName(self):
        return self.nameTraukinys

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
                    self.bendraKroviniuMase += masKrov
                    if vagonas.getVagonasLaisvaMase() == 0:
                        return print("Pavyko prideti, vagonas %s jau pilnas" %(vagonas.getVagonasName()))
                    else:
                        return print("pavyko prideti krovini i %s dar liko %s vietos siame vagone  "%(vagonas.getVagonasName(),
                                                                                   vagonas.getVagonasLaisvaMase()))
            return print("nepavyko prideti, reikia didesniu vagonu")
 
    def saveTraukinys(self):
        name = self.getTrainName()
        with open('%s.json' % name, 'w') as fp:
            lokomotyvai = {}
            
            vagonai = {}
##            for vagonas in self.vagonai:
##                vagonas["%s"],
##                vagonas[],
##                vagonas[],
##                vagonas[],
##                vagonas[],
            data = {"name":self.nameTraukinys,
                    "bendra_mase_kroviniu":self.bendraKroviniuMase,
                    "galia_traukinio":self.galiaTrauk,
                    "bendra mase traukinio":self.bendraMase,
                    "lokomotyvai":lokomotyvai
                                   ##   "vagonai":self.vagonai,
                    }

                lokomotyvas in self.lokomotyvai:
                    lokomotyvas.getLokName = {}
                    lokomotyvas.getLokName["%s"% lokomotyvas.getLokName()] = lokomotyvas.getLokName()
                    lokomotyvas.getLokName["Lokomotyvas_%s_mase" % lokomotyvas.getLokName()] = lokomotyvas.getLokMase()
                    lokomotyvas.getLokName["Lokomotyvas_%s_galia" % lokomotyvas.getLokName()] = lokomotyvas.getLokGalia()
                
                        
                   ## "lokomotyvai":self.lokomotyvai,

            
                
            json.dump(data, fp)
        

             
            
    
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
    
a = Traukinys("Australian_road_train")
a.addLokomotyvas(" Antano_loko ",100,500)
a.addLokomotyvas("Petro_loko", 80,300)
a.addLokomotyvas("Smetonos_loko",100,500)
##print(a.getLokomotyvas)
a.addVagonas("vagons1",40,500)
##import pdb; pdb.set_trace()
a.addVagonas("vagons_2",50,300)
a.addVagonas("rimtas",50,500)
a.pakrautiKrovini(500)
a.pakrautiKrovini(100)
a.pakrautiKrovini(200)
a.saveTraukinys()
##print (a.bendraMase)

