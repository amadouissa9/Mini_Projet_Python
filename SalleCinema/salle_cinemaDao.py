import database
from SalleCinema.salle_Cinema import salle_Cinema
class salle_cinemaDao:
    connexion = database.Connexion()
    cursor = connexion.cursor()
    @classmethod
    def ajouter_salle_cinema(cls,nom_salle,place_salle):
        try:
            sql = "INSERT INTO salle_cinema (Nom_Salle,Place_Salle) VALUES (%s, %s)"
            valeur = (nom_salle, place_salle)
            cls.cursor.execute(sql, valeur)
            cls.connexion.commit()
            sms = "la salle a ete bien enregistrer!!! !"
        except Exception as e:
            sms = f"Une erreur s'est produite lors de l'enregistrement : {e}"
        return sms
    
    @classmethod
    def modifier_salle_cinema(cls, Id_Cinema, nouveau_nom_salle, nouvelle_place_salle):
        if cls.verifier_existence_salle_cinema(Id_Cinema):
            try:
                sql = f"UPDATE salle_cinema SET Nom_Salle = %s, Place_Salle = %s WHERE Id_Cinema = {Id_Cinema}"
                valeurs = (nouveau_nom_salle, nouvelle_place_salle)
                cls.cursor.execute(sql,valeurs)
                cls.connexion.commit()
                sms = "La salle a été modifiée avec succès!"
            except Exception as e:
                sms = f"Une erreur s'est produite lors de la modification de la salle : {e}"
        else:
            sms = "La salle spécifiée n'existe pas dans la base de données."
        print(sms)

    @classmethod
    def verifier_existence_salle_cinema(cls, Id_Cinema):
        try:
            sql = "SELECT COUNT(*) FROM salle_cinema WHERE Id_Cinema = %s"
            cls.cursor.execute(sql, (Id_Cinema,))
            count = cls.cursor.fetchone()[0]
            if count > 0:
                return True  
            else:
                return False  
        except Exception as e:
            return False  
        
    @classmethod
    def supprimer_salle_cinema(cls, Id_Cinema):
        if cls.verifier_existence_salle_cinema(Id_Cinema):
            try:
                sql = f"DELETE FROM salle_cinema WHERE Id_Cinema = {Id_Cinema}"
                cls.cursor.execute(sql)
                cls.connexion.commit()
                sms = "La salle de cinéma a été supprimée avec succès."
            except Exception as e:
                sms = f"Une erreur s'est produite lors de la suppression de la salle de cinéma : {e}"
        else:
            sms = "La salle de cinéma spécifiée n'existe pas dans la base de données."
        return sms

    @classmethod
    def saisie_salle_cinema(cls):
        nom_salle = input("Entrez le nom de la salle de cinéma : ")
        place_salle = int(input("Entrez le nombre de places dans la salle de cinéma : "))
        return nom_salle, place_salle