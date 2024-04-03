import database

class Fille_attenteDao:
    connexion = database.Connexion()
    cursor = connexion.cursor()

    @classmethod
    def verifier_existence_personne(cls, Id_personne):
        try:
            sql = "SELECT COUNT(*) FROM listepersonne WHERE Id_Personne = %s"
            cls.cursor.execute(sql, (Id_personne,))
            count = cls.cursor.fetchone()[0]
            return count > 0  # Retourne True si l'ID existe, sinon False
        except Exception as e:
            return False  # En cas d'erreur, retourne False

    @classmethod
    def ajouter_personne_en_attente(cls, Id_personne):
        if cls.verifier_existence_personne(Id_personne):
            try:
                sql = """
                    INSERT INTO filleattente (Id_Personne)
                    SELECT lp.Id_Personne
                    FROM listepersonne lp
                    LEFT JOIN filleattente ft ON lp.Id_Personne = ft.Id_Personne
                    WHERE ft.Id_Personne IS NULL;
                """
                cls.cursor.execute(sql)
                cls.connexion.commit()
                sms = f"L'identifiant {Id_personne} a été ajouté dans la liste d'attente avec succès."
            except Exception as e:
                sms = f"Une erreur s'est produite lors de l'ajout de l'identifiant {Id_personne} : {e}"
        else:
            sms = f"Impossible d'ajouter l'identifiant {Id_personne} car il n'existe pas dans la liste des personnes."
        print(sms)

    @classmethod
    def supprimer_personne_en_attente(cls, Id_personne):
        try:
            if cls.verifier_existence_personne(Id_personne):
                sql = f"""
                    DELETE lp, ft
                    FROM listepersonne lp
                    LEFT JOIN filleattente ft ON lp.Id_Personne = ft.Id_Personne
                    WHERE lp.Id_Personne = {Id_personne};
                """
                cls.cursor.execute(sql)
                cls.connexion.commit()
                sms = "Toutes les informations ont été supprimées avec succès."
            else:
                sms = "Impossible de supprimer les informations car l'Id_personne spécifié n'existe pas dans la liste des personnes."
        except Exception as e:
            sms = f"Une erreur s'est produite lors de la suppression des informations : {e}"
        print(sms)
