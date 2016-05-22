import doctest
from lokomotyvas import Lokomotyvas
from vagonas import Vagonas
import json
import codecs


class Traukinys():

    def __init__(self, name):
        """test init
	>>> a = Traukinys("Traukinys")
        >>> print(a)
        traukinys: Traukinys, Dabartine sastato mase: 140,
                           galia: 500, bendra kroviniu mase 0
                           lokomotyvu = 1, vagonu = 1      
        ##a = Traukinys("traukinys2")
        >>> a.addLokomotyvas(" Antano_loko ",100,500)
        lokomotyvas sekmingai pridetas
        >>> a.addVagonas("vagons1",40,500, 350)
        vagonas sekmingai pridetas
        >>> print(a)
        traukinys: Traukinys, Dabartine sastato mase: 140,
                           galia: 500, bendra kroviniu mase 0
                           lokomotyvu = 1, vagonu = 1
        
        >>> a.pakrautiKrovini(100)
        pavyko prideti krovini i vagons1 dar liko 400 vietos siame vagone

        

        
	"""
        self.nameTraukinys = name
        self.lokomotyvai = []
        self.vagonai = []
        self.bendraKroviniuMase = 0
        self.galiaTrauk = 0
        self.bendraMase = 0

    def addLokomotyvas(self, name, mase, tempGalia):
        if tempGalia >= mase:
            self.lokomotyvai.append(Lokomotyvas(name, mase, tempGalia))
            self.galiaTrauk += tempGalia
            self.bendraMase += mase
            print("lokomotyvas sekmingai pridetas")
        else:
            return print("lokomotyvo tempiamoji galia negali buti mazesne uz jo mase")

    def addVagonas(self, name, mase, maxMase, ID):
        if self.galiaTrauk < self.bendraMase + mase:
            return print("virsyta mase, kuria gali tempti dabartiniai lokomotyvai")
        else:
            self.vagonai.append(Vagonas(name, mase, maxMase, ID))
            self.bendraMase += mase
            print("vagonas sekmingai pridetas")

    def setTrainStats(self, mase, maseK, galia):
        self.bendraKroviniuMase = maseK
        self.galiaTrauk = galia
        self.bendraMase = mase

    def getGaliaTrauk(self):
        return print("traukinio bendroji tempemoji galia : %s" % (self.galiaTrauk))

    def galiaTrauk(self):
        return self.galiaTrauk

    def maseTrauk(self):
        return self.bendraMase

    def bendraKrovMaseTrauk(self):
        return self.bendraKroviniuMase

    def getLokomotyvas(self):
        return self.lokomotyvai

    def getVagonas(self):
        return self.vagonai

    def getTrainName(self):
        return self.nameTraukinys

    def __str__(self):
        return """traukinys: %s, Dabartine sastato mase: %s,
                   galia: %s, bendra kroviniu mase %s
                   lokomotyvu = %s, vagonu = %s""" % (self.nameTraukinys,
                                                      self.bendraMase,
                                                      self.galiaTrauk,
                                                      self.bendraKroviniuMase,
                                                      len(self.lokomotyvai),
                                                      len(self.vagonai))

    def __repr__(self):
        return "<%s>" % (self.nameTraukinys)

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
                        return print("Pavyko prideti, vagonas %s jau pilnas" % (vagonas.getVagonasName()))
                    else:
                        return print("pavyko prideti krovini i %s dar liko %s vietos siame vagone" % (vagonas.getVagonasName(),
                                                                                                        vagonas.getVagonasLaisvaMase()))
            return print("nepavyko prideti, reikia didesniu vagonu")


def saveTraukinys(traukiniai):
    with open('traukiniai.json', 'w') as fp:
        for traukinys_item in traukiniai:
            lok_list = []
            for lokomotyvas in traukinys_item.lokomotyvai:
                lokomotyvai = {}
                lokomotyvai = {
                    "lokomotyvas": lokomotyvas.getLokName(),
                    "mase": lokomotyvas.getLokMase(),
                    "galia": lokomotyvas.getLokGalia()}
                lok_list.append(lokomotyvai)

            vag_list = []
            for vagonas in traukinys_item.vagonai:
                vagonai = {}
                vagonai = {
                    "vagonas": vagonas.getVagName(),
                    "mase": vagonas.getVagMase(),
                    "max_mase": vagonas.getVagMaxMase(),
                    "kroviniu_mase": vagonas.getVagMaseKroviniu(),
                    "ID": vagonas.getVagId()}
                vag_list.append(vagonai)

            traukinys = {
                "traukinys": traukinys_item.nameTraukinys,
                "bendra_mase_kroviniu": traukinys_item.bendraKroviniuMase,
                "galia_traukinio": traukinys_item.galiaTrauk,
                "bendra_mase_traukinio": traukinys_item.bendraMase,
                "lokomotyvai": lok_list,
                "vagonai": vag_list
            }
            json.dump(traukinys, fp)
            fp.write("\n")
    fp.close()

    def __sub__(a, b):
        return a - b


def openTraukinys():
    data = []
    return_listas = []
    with open('traukiniai.json', 'r') as f:
        for line in f:
            data.append(json.loads(line))

        for item in data:
            new_train = Traukinys(item["traukinys"])
            new_train.setTrainStats(item["bendra_mase_traukinio"],
                                    item["bendra_mase_kroviniu"],
                                    item["galia_traukinio"])
            for vagonas in item["vagonai"]:
                temp_vagonas = Vagonas(vagonas["vagonas"], vagonas["mase"],
                                       vagonas["max_mase"], vagonas["ID"])
                temp_vagonas.setMasKrov(vagonas["kroviniu_mase"])
                new_train.vagonai.append(temp_vagonas)

            for lokomotyvas in item["lokomotyvai"]:
                temp_lokomotyvas = Lokomotyvas(lokomotyvas["lokomotyvas"], lokomotyvas["mase"],
                                               lokomotyvas["galia"])
                new_train.lokomotyvai.append(temp_lokomotyvas)
            return_listas.append(new_train)
        return return_listas


# def __repr__(self):
# return "Vagonas: %s, mase = %s" %(self.name, self.mase, )

   # def __unicode__(self):
    #    return self.name

    def __len__(self,):
        return self._len__

    def get_id(self):
        return id

##a = Traukinys("traukinys2")
##a.addLokomotyvas(" Antano_loko ",100,500)
##a.addVagonas("vagons1",40,500, 350)
##print(a)
# saveTraukinys(listas)
######import pdb; pdb.set_trace()
# a.pakrautiKrovini(100)
# a.saveTraukinys()
####b = openTraukinys()
# print(b)
########print ("bendra mase", a.bendraMase)
######
##listas = openTraukinys()

if __name__ == "__main__":
	doctest.testmod()
