import re  # Importer le module de correspondance de motifs (regex)

class ListePersonne:
    def __init__(self, nom, age, email):
        self.__nom = nom
        self.__age = age
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if re.match(r"[^@]+@[^@]+\.[^@]+", value):
            self.__email = value
        else:
            print("Adresse e-mail invalide. Veuillez saisir une adresse e-mail valide.")

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
