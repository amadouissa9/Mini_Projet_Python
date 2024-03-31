import mysql.connector as mysql

def Connexion():   
            return mysql.connect(
            host="localhost",
            user="root",
            password="",
            database="mini_projet_python"
            )