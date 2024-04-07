import database
from Reservation.reservation import reservation
class reservation_Dao():
    connexion = database.Connexion()
    cursor = connexion.cursor()
    @classmethod
    def reservation_place(cls, nom_salle, id_personne, nom_personne):
        try:
            nom_recupere = cls.recuperation_nom(id_personne)
            if nom_recupere and nom_recupere == nom_personne:
                sql = "INSERT INTO reservation (Nom_Salle, Id_Personne, Nom) VALUES (%s, %s, %s)"
                valeurs = (nom_salle, id_personne, nom_recupere)
                cls.cursor.execute(sql, valeurs)
                cls.connexion.commit()
                sms = "La réservation a été effectuée avec succès !"
            else:
                sms = f"Erreur de réservation : Le nom{nom_personne} de la personne n'existe pas dans la base de données."
        except Exception as e:
            sms = f"Une erreur s'est produite lors de votre réservation : {e}"
        print(sms)



    
    @classmethod
    def recuperation_nom(cls, id_personne):
        sql = "SELECT Nom FROM listepersonne WHERE Id_Personne = %s"
        cls.cursor.execute(sql, (id_personne,))
        nom = cls.cursor.fetchone()
        if nom:
            return nom[0]
        else:
            return f"l'identifiant{id_personne} n'existe pas "
        
    @classmethod
    def places_reservees(cls, Id_Cinema):
        places_reservees = []
        places_totales = reservation_Dao.recuperation_des_places(Id_Cinema)
        try:
            for place in range(1, places_totales + 1):
                reservation = cls.recuperation_des_places(Id_Cinema, place)
                if isinstance(reservation, str):
                    places_reservees.append(place)
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des places réservées: {e}") 
        if places_reservees:
            print("Places réservées : ", places_reservees)
        else:
            print("Aucune place n'est réservée.")
        
        return places_reservees

    @classmethod
    def places_disponibles(cls, Id_Cinema):
        places_disponibles = []
        max_place = reservation_Dao.recuperation_des_places(Id_Cinema)
        for place in range(1, max_place + 1):
            try:
                place_existe = cls.recuperation_des_places(place)
                if isinstance(place_existe, str):
                    places_disponibles.append(str(place))  
            except Exception as e:
                print(f"Une erreur s'est produite lors de la vérification de la place {place}: {e}")
        return places_disponibles

    @classmethod
    def recuperation_des_places(cls, Id_Cinema):
        sql = "SELECT Place_Salle FROM salle_cinema WHERE Id_Cinema = %s"
        cls.cursor.execute(sql, (Id_Cinema,))
        place = cls.cursor.fetchone()
        if place:
            return place[0]  
        else:
            return f"le Place_Salle:{place} n'existe pas dans la liste des personnes "

    @classmethod
    def filtrer_reservations_par_nom(cls, nom):
        try:
            sql = "SELECT * FROM reservation WHERE Nom = %s"
            cls.cursor.execute(sql, (nom,))
            reservations = cls.cursor.fetchall()
            return reservations
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des réservations : {e}")
            return []
    
    @classmethod
    def recuperer_nom_reservation(cls, nom):
        try:
            sql = "SELECT Nom FROM reservation WHERE Nom = %s"
            cls.cursor.execute(sql, (nom,))
            nom_trouve = cls.cursor.fetchone()

            if nom_trouve:
                return nom_trouve[0] 
            else:
                return f"le Nom:{nom} m'existe pas dans les reservations"
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération du nom de la réservation : {e}")
            return None
    
    @classmethod
    def annuler_reservation_par_nom(cls, nom):
        nom_reservation = cls.recuperer_nom_reservation(nom)
        
        if nom_reservation:
            try:
                sql_suppression = "DELETE FROM reservation WHERE Nom = %s"
                cls.cursor.execute(sql_suppression, (nom,))
                cls.connexion.commit()
                return f"La réservation pour {nom_reservation} a été annulée avec succès."
            except Exception as e:
                return f"Une erreur s'est produite lors de l'annulation de la réservation. {e}"
        else:
            return f"Aucune réservation trouvée pour {nom}."

    @classmethod
    def saisit_reservation(cls):
        try:
            nom_salle = input("Entrez le Nom de la salle : ")
            id_personne = input("Entrez l'identifiant de la personne : ")
            nom_personne = cls.recuperation_nom(id_personne)
            if nom_personne:
                print(f"Nom de la personne : {nom_personne}")
                confirmation = input("Confirmez-vous le nom de la personne ? (O/N) : ")
                if confirmation.upper() == "O":
                    return nom_salle, id_personne, nom_personne
                else:
                    print("Saisie annulée.")
                    return None
            else:
                raise ValueError("Erreur : Aucun nom trouvé pour l'identifiant de la personne donné.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la saisie de la réservation : {e}")