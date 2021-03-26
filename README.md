# Une-infra-dans-le-Cloud

### objectif: 

* Mettre en place une infrastructure qui doit inclure dans un premier temps, une base PostgreSQL sur RDS.
* Créer une API proposant l'accès à cette base sur EC2. 
* Sauvegarder le fichier SQL servant à créer la base sur S3.

## 1. Création de la bdd PostgresSQL sur AWS RDS.

On va Configurer un serveur PostgreSQL sur RDS, à partir de votre compte IAM d’AWS. 
une fois les paramètres de sécurité effectué, on va créer un docker compose avec une image postgres et une autre pgadmin.
Le lancement du docker compose nous permet d'accéder directement à pgAdmin (localhost:8080) et de visualiser la bdd.
