from ListePersonnes.ListePersonneDao import ListePersonneDao
from FilleAttentes.Fille_attenteDao import Fille_attenteDao
import database

class Menu:
    @staticmethod
    def afficher_menu():
        print("\n Menu de Parti 1:")
        print("1. Ajouter une personne")
        print("2. Afficher toutes les personnes")
        print("3. Rechercher une personne par nom")
        print("4. Filtrer les personnes par âge")
        print("5. Ajouter une personne en attente")
        print("6. Supprimer une personne en attente e liste")
        print("7. Quitter")

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
            print("Au revoir !")
        else:
            print("Choix invalide, veuillez sélectionner une option valide.")

if __name__ == "__main__":
    while True:
        Menu.afficher_menu()
        choix = int(input("Entrez votre choix : "))
        Menu.executer_action(choix)

