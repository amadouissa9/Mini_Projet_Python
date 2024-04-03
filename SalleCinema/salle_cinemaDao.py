import database
from SalleCinema.salle_Cinema import salle_Cinema
class salle_cinemaDao:
    connexion = database.Connexion()
    cursor = connexion.cursor()
    @classmethod
    def ajouter_salle_cinema(cls,)