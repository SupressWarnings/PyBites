from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self._expired = expires < NOW

    def getexpired(self):
        return self._expired

    def setexpired(self, new):
        self._expired = new

    def delexpired(self):
        del self._expired

    expired = property(getexpired, setexpired, delexpired)
