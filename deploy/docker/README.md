# Docker

## Qu'est-ce que Docker ?

Docker est une plateforme de conteneurisation qui permet de packager des applications et leurs dépendances dans un environnement léger et isolé, appelé conteneur. Contrairement aux machines virtuelles (VMs), Docker partage le noyau du système d'exploitation hôte, ce qui le rend plus léger et plus rapide.

```bash
# installation (Sur macOS et Windows : Téléchargez Docker Desktop.)
sudo apt-get install docker-ce docker-ce-cli containerd.io
# version
sudo docker version
# information sur la configuration
sudo docker info
# Pour utiliser Docker sans les droits root , l’utilisateur doit appartenir appartenir au groupe docker
sudo groupadd docker
sudo usermod -aG docker $USER

```

## concepts

- Image Docker : Un modèle statique qui contient le code source, les dépendances, et l'environnement nécessaire pour exécuter une application.
- Conteneur Docker : Une instance en cours d'exécution d'une image.
- Docker Hub : Un registre où vous pouvez trouver des images Docker prêtes à l'emploi.

## Lancer un conteneur

La commande docker run qui permet de lancer un conteneur peut également télécharger l’image si elle n’est pas disponible localement

```bash
docker run debian:stretch
# Connaitre l’historique de création de l’image 
docker history debian
# Lister les images présentent localement
docker images
# Ajouter un tag à une image 
docker image tag debian:stretch debian:levasbr1
# Supprimer une image
docker rmi debian:latest
# creer un container
docker run -it nom_image
# Lister les conteneurs en cours d’exécution
docker ps
# obtenir la liste complete
docker ps -a
# Obtenir une session intéractive 
docker run -it debian:latest /bin/bash
# Lancer un conteneur en mode daemon (arriere plan)
docker run -d --name test_daemon nginx
# Obtenir la configuration détaillée d’un conteneur
docker inspect <nom_conteneur> ou <CID>
# Récupérer la sortie standard d’un conteneur
docker logs <nom_conteneur> ou <CID>
# Afficher les processus en cours dans un conteneur
docker top <nom_conteneur> ou <CID>
# Suspendre (freezer) et réactiver un conteneur
docker pause / unpause <nom_conteneur> ou <CID>
# Arrêter / démarrer / tuer / redémarrer un conteneu
docker stop / start / kill / restart <nom_conteneur> ou <CID>
# Exporter l’ensemble du système de fichier d’un conteneur dans une archive TAR
docker export <nom_conteneur> ou <CID> > archive.tar
# Afficher les ports réseaux exposés par un conteneur
docker port <nom_conteneur> ou <CID>
# Afficher les changements effectués sur les fichiers d’un conteneur (A=Ajout, D=Delete, C=Modif )
docker run -it --name test_diff debian /bin/bash
# Exécuter une commande dans un conteneur démarré
#Dans l’exemple, on lance un conteneur nginx en mode daemon et on utilise la commande docker exec pour s’y connecter
docker run -d --name test_exec nginx
docker exec -it test_exec /bin/bash
# Supprimer un conteneur (il doit être arrêté...)
docker rm test_attach
# Copier des fichiers depuis ou à destination d’un conteneur
docker cp <src> <des>
# Afficher des informations sur les conteneurs exécutés par Docker (équivalent à un top sous Linux)
docker stats
# Afficher les événements qui se produisent sur le bus du moteur Docker (équivalent à un tailf sur un fichier de log)
docker events
```

## Dockerfile

Un Dockerfile est un fichier texte contenant les instructions pour construire une image Docker.

```bash
# Utiliser une image de base
FROM ubuntu:latest
# Installer les dépendances
RUN apt-get update && apt-get install -y python3
RUN apt-get install -y nginx
# Copier les fichiers locaux
COPY . /app
# Définir le répertoire de travail
WORKDIR /app
# Exécuter le script Python
CMD ["python3", "script.py"]

# Générer une image à partir d’un dockerfile 
docker build -t mon_image .
# creer un volume
docker volume create nom_volume
# utiliser un volume
docker run -v nom_volume:/chemin_dans_conteneur nom_image
# On peut ensuite lancer un conteneur depuis cette nouvelle image
docker run -d -p 8002:80 --name test_build levasbr1/nginx:latest
# Lister les réseaux
docker network ls
# Créer un réseau
docker network create mon_reseau
# Lancer un conteneur sur un réseau spécifique
docker run --network=mon_reseau nom_image

```

Niveau 3 : Avancé
3.1. Docker Compose
Docker Compose permet de gérer plusieurs conteneurs à la fois avec un fichier YAML.

Exemple de fichier docker-compose.yml :

yaml
Copy code
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: example
Commande pour lancer le tout :

bash
Copy code
docker-compose up
3.2. Optimisation des Dockerfiles
Minimiser la taille de l’image : Utiliser des images de base légères comme alpine.
Utiliser le cache de Docker : Docker optimise les builds en utilisant le cache des couches précédentes.
3.3. Sécurisation de Docker
Exécuter les conteneurs en tant qu'utilisateur non-root pour limiter l'accès.
Utiliser les secrets Docker pour gérer les informations sensibles (mots de passe, tokens).
3.4. Déploiement de Docker en production
Utiliser un orchestrateur de conteneurs comme Kubernetes ou Docker Swarm pour gérer des clusters de conteneurs.
Monitoring et logging avec des outils comme Prometheus, Grafana et ELK Stack (Elasticsearch, Logstash, Kibana).
Niveau 4 : Expert
4.1. Docker Swarm
Docker Swarm est une plateforme d'orchestration de conteneurs intégrée dans Docker.

Initier un Swarm : docker swarm init
Ajouter des nœuds : docker swarm join-token worker
Déployer une application dans le Swarm : docker stack deploy -c docker-compose.yml mon_stack
4.2. CI/CD avec Docker
Automatiser les déploiements avec Docker en utilisant un pipeline CI/CD.

Intégration avec des outils comme Jenkins, GitLab CI, ou GitHub Actions pour automatiser la création et le déploiement d’images Docker.
4.3. Multistage Builds
Les builds multi-étapes permettent de créer des images Docker légères en séparant les phases de construction et d'exécution dans plusieurs étapes.

Exemple :

Dockerfile
Copy code
# Étape 1 : Build
FROM golang AS builder
WORKDIR /app
COPY . .
RUN go build -o app .

# Étape 2 : Exécution
FROM alpine
WORKDIR /app
COPY --from=builder /app/app .
CMD ["./app"]

4.4. Monitoring et scaling avancé
Utiliser des outils de monitoring pour surveiller les ressources des conteneurs : cAdvisor, Prometheus.
Utiliser un auto-scaling pour ajuster dynamiquement le nombre de conteneurs en fonction de la charge.
4.5. Clusters Kubernetes
Intégration de Docker avec Kubernetes pour gérer des conteneurs à grande échelle dans des clusters répartis. Vous apprendrez à :

Déployer un cluster Kubernetes avec kubectl.
Gérer des conteneurs avec des Pods, Services, et Deployments.
