import doctest
class Vagonas:

    def __init__(self, name, mase, maxMase, ID):
        """test init
	>>> a = Vagonas("vagonas",10,100,500)
        >>> print(a)
        pavadinimas = vagonas, mase  = 10, maksimali mase= 100, mase kroviniu = 0
        >>> a.getVagName()
        'vagonas'
        >>> a.getVagMase()
        10
        >>> a.getVagMaxMase()
        100
        >>> a.getVagMaseKroviniu()
        0
        >>> a.getVagId()
        500
	"""
        self.name = name
        self.mase = mase
        self.maxMase = maxMase
        self.ID = ID
        self.maseKroviniu = 0

    def __str__(self):
        return "pavadinimas = %s, mase  = %s, maksimali mase= %s, mase kroviniu = %s" % (self.name,
                                                                        self.mase,
                                                                        self.maxMase,
                                                                        self.maseKroviniu )
    def addKrovinys(self, maseKrov):
        if self.maxMase >= maseKrov + self.maseKroviniu:
            self.maseKroviniu += maseKrov
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

    def getVagonasName(self):
        return self.name

    def getVagonasLaisvaMase(self):
        return self.maxMase - self.maseKroviniu

    def __repr__(self):
        return "%s" % (self.name)

    def __unicode__(self):
        return self.name

    def __len__(self,):
        return self._len__

    def get_id(self):
        return id


if __name__ == "__main__":
	doctest.testmod()


