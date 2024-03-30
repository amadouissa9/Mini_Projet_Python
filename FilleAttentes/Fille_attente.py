class Fille_attente:
    def __init__(self,Id_personne):
        self.__Id_personne = Id_personne

    @property
    def Id_personne(self):
        return self.__Id_personne

    @Id_personne.setter
    def _Id_personne(self, value):
        self.__Id_personne = value

       
