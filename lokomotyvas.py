import doctest
class Lokomotyvas:

    def __init__(self, name, mase, tempGalia):
        """test init
	>>> a = Lokomotyvas("lokomotyvas",10,1000)
        >>> print(a)
        Lokomotyvas = lokomotyvas  Mase = 10, tempiamoji galia = 1000
        
        >>> a.getLokName()
        'lokomotyvas'
        >>> a.getLokMase()
        10
        >>> a.getLokGalia()
        1000
	"""

        self.name = name
        self.mase = mase
        self.tempGalia = tempGalia

    def __sub__(a, b):
        return a - b

    def getLokName(self):
        return self.name

    def getLokMase(self):
        return self.mase

    def getLokGalia(self):
        return self.tempGalia

    def __repr__(self):
        return "%s" % (self.name)

    def __str__(self):
        return "Lokomotyvas = %s  Mase = %s, tempiamoji galia = %s" % (self.name, self.mase, self.tempGalia)
       

if __name__ == "__main__":
	doctest.testmod()
