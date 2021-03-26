from typing import Optional
from fastapi import FastAPI

#from data import DataAccess

import uvicorn


#Psycopg est l' adaptateur de base de données PostgreSQL le plus populaire pour le langage de programmation Python.

import psycopg2

class DataAccess():


  
    @classmethod
    #connection à la bdd postgres "exercises"
    def connexion(cls):
          
        cls.connect = psycopg2.connect(host="database-2.cpq3kqdrmhhx.us-east-2.rds.amazonaws.com", database="exercises", user="postgres", password="pgadmin2")
        
         # création du curseur 
        cls.cursor = cls.connect.cursor()
        
	    # exécuter une instruction
        print('PostgreSQL database version:')
        cls.cursor.execute('SELECT version()')

        # afficher la version du serveur de base de données PostgreSQL
        cls.db_version =cls.cursor.fetchone()
        print(cls.db_version)
        
    @classmethod
    def close_db(cls):
        cls.connect.close()
        cls.cursor.close()

 

    #afficher les tables de la datbase    
    #@classmethod
    #def tables(cls):    
    #    cls.cursor.execute(" select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        # cur.execute('SELECT * FROM facilities')
    #    data = cls.cursor.fetchone()
    #    cls.close_db()
    #    return data
        

    #Afficher une liste d'informations des membres de la table facilities.
    @classmethod
    def member(cls):
        cls.connexion()
        cls.cursor.execute('select surname,firstname,address,telephone from cd.members')
        data = cls.cursor.fetchall()
        cls.close_db()
        #return {'members': {'surname': data['surname'],'firstname': data['firstname']}}
        return data


    #Afficher le prénom et le nom du ou des derniers membres qui se sont inscrits - pas seulement la date.
    # #@classmethod
    # def last_member(cls):
    #     cls.connexion()
    #     cls.cursor.execute('select firstname, surname, joindate from cd.members where joindate = (select max(joindate) from cd.members)')
    #     data = cls.cursor.fetchone()
    #     cls.close_db()
    #     return {'member': {'firstname': data['firstname'],'surname': data['surname'],'joindate':data['joindate']}}


    #Afficher une liste ordonnée des 10 premiers noms de famille dans le tableau des membres? 
    #La liste ne doit pas contenir de doublons.
    @classmethod
    def first_10(cls):
        cls.connexion()
        cls.cursor.execute('select distinct surname from cd.members order by surname asc limit 10')
        data = cls.cursor.fetchall()
        cls.close_db
        return data
        #return {'member':{'surname':data['surname']}}

    

         


# print('===========================================')
# member = DataAccess().member()
# print(member)
# print('===========================================')
# first = DataAccess().first_10()
# print (first)
# print('===========================================')




app = FastAPI()

@app.get("/")
def index():
    return {"Hello":"World"}


#Afficher le prénom et le nom du ou des derniers membres qui se sont inscrits - pas seulement la date.
@app.get("/api/last/", tags=['Informations membres facilities'])
async def last():
    return DataAccess.member()

#Afficher une liste ordonnée des 10 premiers noms de famille dans le tableau des membres?
@app.get("/api/first/", tags=['Informations 10 premiers membres'])
async def first():
    return DataAccess.first_10()




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8800)




