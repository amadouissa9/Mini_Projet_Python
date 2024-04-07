from ListePersonnes.ListePersonneDao import ListePersonneDao
from FilleAttentes.Fille_attenteDao import Fille_attenteDao
from SalleCinema.salle_cinemaDao import salle_cinemaDao
from Reservation.reservationDao import reservation_Dao
import database

class Menu:
    @staticmethod
    def afficher_menu():
        print("\n Menu de Parti :")
        print("1. Ajouter une personne")
        print("2. Afficher toutes les personnes")
        print("3. Rechercher une personne par nom")
        print("4. Filtrer les personnes par âge")
        print("5. Ajouter une personne en attente")
        print("6. Supprimer une personne en attente de la liste")
        print("7. Ajouter une salle de cinéma")
        print("8. Modifier une salle de cinéma")
        print("9. Supprimer une salle de cinéma")
        print("10. Réserver une place")
        print("11. Annuler une réservation")
        print("12. Afficher les places disponibles")
        print("13. Afficher les places réservées")
        print("14. Quitter")

    @staticmethod
    def executer_action(choix):
        if choix == 1:
            nom, age = ListePersonneDao.saisie_personne()
            print(ListePersonneDao.Ajouter_personne(nom, age))
        elif choix == 2:
            print(ListePersonneDao.Affiche_personne())
        elif choix == 3:
            nom = input("Entrez le nom de la personne à rechercher : ")
            print(ListePersonneDao.Rechercher_personne_par_nom(nom))
        elif choix == 4:
            age_min = int(input("Entrez l'âge minimum : "))
            age_max = int(input("Entrez l'âge maximum : "))
            print(ListePersonneDao.Filtrer_personnes_par_age(age_min, age_max))
        elif choix == 5:
            Id_personne = int(input("Entrez l'Id de la personne à ajouter en attente : "))
            Fille_attenteDao.ajouter_personne_en_attente(Id_personne)
        elif choix == 6:
            Id_personne = int(input("Entrez l'Id de la personne à supprimer : "))
            Fille_attenteDao.supprimer_personne_en_attente(Id_personne)
        elif choix == 7:   
            nom_salle,place_salle = salle_cinemaDao.saisie_salle_cinema()
            print(salle_cinemaDao.ajouter_salle_cinema(nom_salle,place_salle))
        elif choix == 8:
            Id_Cinema = int(input("Entrez identifiant de la salle a modifier : "))
            nouveau_nom_salle, nouvelle_place_salle = salle_cinemaDao.saisie_salle_cinema()
            print(salle_cinemaDao.modifier_salle_cinema(Id_Cinema, nouveau_nom_salle, nouvelle_place_salle))
        elif choix == 9:
           Id_Cinema = int(input("Entrez identifiant de la salle a supprimer : ")) 
           print(salle_cinemaDao.supprimer_salle_cinema(Id_Cinema))
        elif choix == 10:
            nom_salle,id_personne,nom_personne = reservation_Dao.saisit_reservation()
            print(reservation_Dao.reservation_place(nom_salle,id_personne,nom_personne))
        elif choix == 11:
            nom = input("Entrez le nom de la réservation à annuler : ")
            print(reservation_Dao.annuler_reservation_par_nom(nom))
        elif choix == 12:
            Id_Cinema = input("Entrez l'identifiant de la salle : ")
            print("Les places disponibles sont : ", reservation_Dao.places_disponibles(Id_Cinema))
        elif choix == 13:
            Id_Cinema = input("Entrez l'identifiant de la salle : ")
            print("Les places réservées sont : ", reservation_Dao.places_reservees(Id_Cinema))
        elif choix == 14:
            print("Au revoir")
        else:
            print("Choix invalide, veuillez sélectionner une option valide.")

if __name__ == "__main__":
    while True:
        Menu.afficher_menu()
        choix = int(input("Entrez votre choix : "))
        Menu.executer_action(choix)

