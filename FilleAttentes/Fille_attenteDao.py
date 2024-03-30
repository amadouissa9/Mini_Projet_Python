import database
connexion = database.Connexion()
cursor = connexion.cursor()
class Fille_attenteDao:
    @classmethod
    def verifier_existence_personne(cls, Id_personne):
        try:
            sql = "SELECT COUNT(*) FROM listepersonne WHERE Id_Personne = %s"
            cls.cursor.execute(sql, (Id_personne,))
            count = cls.cursor.fetchone()[0]
            if count > 0:
                return True  # L'Id_personne existe dans la table listepersonne
            else:
                sms = "L'Id_personne spécifié n'existe pas dans la table listepersonne."
                
        except Exception as e:
            sms = f"Une erreur s'est produite lors de la vérification de l'existence de l'Id_personne : {e}"
        return sms
        return False
    @classmethod
    def ajouter_personne_en_attente(cls, Id_personne,):
        if cls.verifier_existence_personne(cls, Id_personne):
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
                print("Les identifiants de personne ont été ajoutés  avec succès.")
            except Exception as e:
                print(f"Une erreur s'est produite lors de l'ajout des identifiants de personne  : {e}")
        else:
            print("Impossible d'ajouter l'Id_personne  car il n'existe pas dans la liste des personnes.")

    @classmethod
    def supprimer_personne_en_attente(cls,Id_personne):
        try:
            if cls.verifier_existence_personne(Id_personne):
                sql = """
                    DELETE lp, ft FROM listepersonne lp
                    LEFT JOIN filleattente ft ON lp.Id_Personne = ft.Id_Personne
                """
                cls.cursor.execute(sql)
                cls.connexion.commit()
                print("Toutes les informations ont été supprimées avec succès.")
            else:
                print("Impossible de supprimer les informations car l'Id_personne spécifié n'existe pas dans la  liste des personnes.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la suppression des informations : {e}")
