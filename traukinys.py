from lokomotyvas import Lokomotyvas
from vagonas import Vagonas
import json
import codecs
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
        data = []
        with open('traukiniai.json','r') as f:
            for line in f:
                data.append(json.loads(line))
                for item in data:
                    if item["traukinys"] == self.nameTraukinys:
                        return print("issaugoti nepavyko, toks traukinys jau yra")
        with open('traukiniai.json' , 'a') as fp:
            traukinys = {
                "traukinys":self.nameTraukinys,
                "bendra_mase_kroviniu":self.bendraKroviniuMase,
                "galia_traukinio":self.galiaTrauk,
                "bendra mase traukinio":self.bendraMase,
                }
            json.dump(traukinys,fp)
            fp.write("\n")
            fp.close()
           
        with open('lokomotyvai.json', 'a') as fp:
            listas = []
            for lokomotyvas in self.lokomotyvai:
                lokomotyvai = {} 
                lokomotyvai = { 
                "traukinys" : self.nameTraukinys,
                "lokomotyvas" : lokomotyvas.getLokName(),
                "mase"  : lokomotyvas.getLokMase(),
                "galia"  : lokomotyvas.getLokGalia()}
                listas.append(lokomotyvai)
                json.dump(listas,fp)
    
        fp.close()
                
        with open('vagonai.json', 'a') as fp:
            listas = []
            for vagonas in self.vagonai:
                vagonai = {}
                vagonai = {
                "traukinys":self.nameTraukinys,
                "vagonas" :vagonas.getVagName(),
                "mase" :vagonas.getVagMase(),
                "max_mase" : vagonas.getVagMaxMase(),
                "kroviniu_mase" : vagonas.getVagMaseKroviniu(),
                "ID" : vagonas.getVagId()}
                listas.append(vagonai)
                json.dump(vagonai,fp)
                
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
    
a = Traukinys("Australian_road_trasdasdaasdasdin")
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

