Introduction à Docker : De débutant à expert
1. Qu'est-ce que Docker ?

Docker est une plateforme de conteneurisation qui permet de packager des applications et leurs dépendances dans un environnement léger et isolé, appelé conteneur. Contrairement aux machines virtuelles (VMs), Docker partage le noyau du système d'exploitation hôte, ce qui le rend plus léger et plus rapide.

Niveau 1 : Débutant
1.1. Installation de Docker
Sur Linux : sudo apt-get install docker-ce docker-ce-cli containerd.io
Sur macOS et Windows : Téléchargez Docker Desktop.
Vérification de l’installation : docker --version
1.2. Concepts de base
Image Docker : Un modèle statique qui contient le code source, les dépendances, et l'environnement nécessaire pour exécuter une application.
Conteneur Docker : Une instance en cours d'exécution d'une image.
Docker Hub : Un registre où vous pouvez trouver des images Docker prêtes à l'emploi.
1.3. Commandes de base
Lister les conteneurs : docker ps
Créer un conteneur : docker run -it nom_image
Exécuter un conteneur en arrière-plan : docker run -d nom_image
Arrêter un conteneur : docker stop ID_conteneur
Supprimer un conteneur : docker rm ID_conteneur
Supprimer une image : docker rmi nom_image
1.4. Exercice : Hello World
Exécutez docker run hello-world pour tester Docker avec une image minimale.
Niveau 2 : Intermédiaire
2.1. Dockerfile : Créer vos propres images
Un Dockerfile est un fichier texte contenant les instructions pour construire une image Docker.

Exemple basique :

Dockerfile
Copy code
# Utiliser une image de base
FROM ubuntu:latest

# Installer les dépendances
RUN apt-get update && apt-get install -y python3

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers locaux
COPY . /app

# Exécuter le script Python
CMD ["python3", "script.py"]
Commande pour construire l’image :

bash
Copy code
docker build -t mon_image .
2.2. Gestion des volumes
Les volumes permettent de persister les données entre les conteneurs et le système hôte.

Créer un volume : docker volume create nom_volume
Utiliser un volume : docker run -v nom_volume:/chemin_dans_conteneur nom_image
2.3. Réseaux Docker
Les conteneurs peuvent communiquer via des réseaux personnalisés.

Lister les réseaux : docker network ls
Créer un réseau : docker network create mon_reseau
Lancer un conteneur sur un réseau spécifique : docker run --network=mon_reseau nom_image
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
