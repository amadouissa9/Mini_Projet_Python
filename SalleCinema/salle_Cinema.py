class salle_Cinema:
    def __init__(self, nomsalle, place):
        self.__nomsalle = nomsalle
        self.__place = place

    @property
    def nomsalle(self):
        return self.__nomsalle

    @nomsalle.setter
    def _nomsalle(self, value):
        self.__nomsalle = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def _place(self, value):
        self.__place = value
