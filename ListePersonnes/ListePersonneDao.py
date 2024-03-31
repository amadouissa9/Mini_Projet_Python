import database
from ListePersonnes.ListePersonne import ListePersonne
connexion = database.Connexion()
cursor = connexion.cursor()

class ListePersonneDao:
    def __init__(self):
        pass

    @classmethod
    def Ajouter_personne(cls, nom, age,email):
        try:
            sql = "INSERT INTO listepersonne (Nom, Age,email) VALUES (%s, %s, %s)"
            valeur = (nom, age, email)
            cls.cursor.execute(sql, valeur)
            cls.connexion.commit()
            sms = "Personne ajoutée avec succès !"
        except Exception as e:
            sms = f"Une erreur s'est produite lors de l'ajout de la personne : {e}"
        return sms

    @classmethod
    def Affiche_personne(cls, ID):
        try:
            sql = "SELECT * FROM listepersonne"
            cls.cursor.execute(sql)
            liste = cls.cursor.fetchall()
            if not liste:
                sms = "Aucune personne à afficher dans votre liste."
            else:
                for row in liste:
                    id, nom, age = row
                    print(f"Identifiant: {id}, Nom: {nom}, Âge: {age}")
        except Exception as e:
            sms = f"Une erreur s'est produite lors de l'affichage des informations de la personne : {e}"
        return sms

    @classmethod
    def Rechercher_personne_par_nom(cls, nom):
        try:
            sql = "SELECT * FROM listepersonne WHERE Nom = %s"
            cls.cursor.execute(sql, (nom,))
            personne = cls.cursor.fetchone()
            if personne:
                id, nom, age, email = personne
                sms = f"Identifiant: {id}, Nom: {nom}, Age: {age}, E-mail: {email}"
            else:
                sms = f"Aucune personne avec le nom : '{nom}' n'a été trouvée."
        except Exception as e:
            sms = f"Une erreur s'est produite lors de la recherche de la personne par nom : {e}"
        return sms

    @classmethod
    def Filtrer_personnes_par_age(cls, age_min, age_max):
        try:
            sql = "SELECT * FROM listepersonne WHERE Age BETWEEN %s AND %s"
            cls.cursor.execute(sql, (age_min, age_max))
            result = cls.cursor.fetchall()
            if not result:
                sms = "Aucune personne trouvée dans cette tranche d'âge."
            else:
                sms = "Personnes dans la tranche d'âge spécifiée :"
                for row in result:
                    id, nom, age = row
                    sms += f"\nIdentifiant: {id}, Nom: {nom}, Âge: {age}"
        except Exception as e:
            sms = f"Une erreur s'est produite lors du filtrage des personnes par âge : {e}"
        return sms
    
    @classmethod
    def saisie_personne(cls):
        try:
            nom = input("Entrez le nom de la personne : ")
            age = int(input("Entrez l'âge de la personne : "))
            email = int(input("Entrez l'âge de la personne : "))
            return nom, age, email
        except ValueError as e:
            print("Erreur : L'âge doit être un nombre entier." ,e)
            return None, None