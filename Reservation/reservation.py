class reservation:
    def __init__(self, nom_Salle, Id_Personne):
        self.__nom_Salle = nom_Salle
        self.__Id_Personne = Id_Personne

    @property
    def nom_Salle(self):
        return self.nom_Salleom_Salle

    @nom_Salle.setter
    def _Nom_Salle(self, value):
        self.nom_Salleom_Salle = value

    @property
    def Id_Personne(self):
        return self.__Id_Personne

    @Id_Personne.setter
    def _Id_Personne(self, value):
        self.__Id_Personne = value


