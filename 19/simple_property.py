from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.expired = expires < NOW
