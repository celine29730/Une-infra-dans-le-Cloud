# Une-infra-dans-le-Cloud

### objectif: 

* Mettre en place une infrastructure qui doit inclure dans un premier temps, une base PostgreSQL sur RDS.
* Créer une API proposant l'accès à cette base sur EC2. 
* Sauvegarder le fichier SQL servant à créer la base sur S3.

## 1. Création de la bdd PostgresSQL sur AWS RDS.

On va Configurer un serveur PostgreSQL sur RDS, à partir de votre compte IAM d’AWS. 
une fois les paramètres de sécurité effectué, on va créer un docker compose avec une image postgres et une autre pgadmin.
Le lancement du docker compose nous permet d'accéder directement à pgAdmin (localhost:8080) et de visualiser la bdd.
[pgAdim](https://github.com/celine29730/Une-infra-dans-le-Cloud/blob/main/bddpgadmin.png)

Le fichier sql "clubdata.sql",est copié sur docker afin de créer la bdd. 

## 2. Mise en place d'un serveur avec EC2 pour accueillir l'appli Python.

Création d'une instance sur AWS EC2 en utilisant la plateforme Amazon Linux.
L'API a été créée grace à FastAPI et propose deux requêtes PostgresSQL (liste d'informations des membres de la table members et les dix premiers membres sans doublons).
Le docker compose permet également de lancer l'API.

La connection au serveur EC2 se fait sur VS code grace la paire de clés créée sur AWS.
les fichiers necessaires pour le fonctionnement de l'API sont copiés sur Vs code en SSH.

En utilisant l'URL de l'instance EC2 http://3.22.249.166:8800/docs, on peut visualiser les réslutats de nos deux requêtes issues de l'API.









