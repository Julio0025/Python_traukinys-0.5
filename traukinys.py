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
        
    def addVagonas(self, name, mase, maxMase, ID):
        if self.galiaTrauk < self.bendraMase + mase:
            return print("virsyta mase, kuria gali tempti dabartiniai lokomotyvai")
        else:
            self.vagonai.append(Vagonas(name,mase,maxMase, ID))
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
        with open('traukiniai.json' , 'a') as fp:
            traukinys = {
                "traukinys":self.nameTraukinys,
                "bendra_mase_kroviniu":self.bendraKroviniuMase,
                "galia_traukinio":self.galiaTrauk,
                "bendra mase traukinio":self.bendraMase,
                }
            fp.write(json.dumps(traukinys))
            fp.write("\n")
            fp.close()
           
        with open('lokomotyvai.json', 'a') as fp:
     	      for lokomotyvas in self.lokomotyvai:
                lokomotyvai = {} 
                lokomotyvai = { 
                "traukinys" : self.nameTraukinys,
                "lokomotyvas" : lokomotyvas.getLokName(),
                "mase"  : lokomotyvas.getLokMase(),
                "galia"  : lokomotyvas.getLokGalia()}
                fp.write(json.dumps(lokomotyvai))
                fp.write("\n")
        fp.close()
                
        with open('vagonai.json', 'a') as fp:
            for vagonas in self.vagonai:
                vagonai = {}
                vagonai = {
                "traukinys":self.nameTraukinys,
                "vagonas" :vagonas.getVagName(),
                "mase" :vagonas.getVagMase(),
                "max_mase" : vagonas.getVagMaxMase(),
                "kroviniu_mase" : vagonas.getVagMaseKroviniu(),
                "ID" : vagonas.getVagId()}
                fp.write(json.dumps(vagonai))
                fp.write("\n")
                
        fp.close()
           
           

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
a.addVagonas("vagons1",40,500, 350)
##import pdb; pdb.set_trace()
a.addVagonas("vagons_2",50,300,123)
a.addVagonas("rimtas",50,500,343)
a.pakrautiKrovini(500)
a.pakrautiKrovini(100)
a.pakrautiKrovini(600)
a.saveTraukinys()
##print (a.bendraMase)

