Kubernetes : De débutant à expert
Introduction à Kubernetes

Kubernetes (K8s) est une plateforme open-source d'orchestration de conteneurs qui automatise le déploiement, la gestion, la mise à l'échelle, et les opérations des applications conteneurisées. Il permet de gérer des clusters de machines et des conteneurs sur une infrastructure distribuée.

Niveau 1 : Débutant
1.1. Concepts de base
Cluster : Ensemble de machines (nœuds) qui exécutent des conteneurs Kubernetes.
Nœud : Machine physique ou virtuelle faisant partie du cluster Kubernetes.
Pod : L'unité de base d'exécution dans Kubernetes. Un Pod contient un ou plusieurs conteneurs qui partagent des ressources comme l'IP, les volumes, etc.
Service : Une abstraction pour exposer les Pods, permettant une communication stable.
Namespace : Isolation logique au sein du cluster pour organiser et sécuriser les ressources.
1.2. Architecture de Kubernetes
Kubernetes utilise une architecture maître/nœud :

Master Node : Coordonne le cluster, gère les déploiements, les échelles et les nœuds.

API Server : Point d'entrée pour toutes les commandes et interactions avec Kubernetes.
Controller Manager : Surveille l'état du cluster et prend des actions correctives.
Scheduler : Assigne des Pods aux nœuds disponibles.
etcd : Base de données clé-valeur distribuée pour stocker l'état du cluster.
Worker Node : Exécute les Pods et communique avec le Master Node.

Kubelet : Processus principal du nœud qui gère les Pods.
Kube-proxy : Gère le routage réseau des Pods.
Container Runtime : Interface pour exécuter des conteneurs (comme Docker ou containerd).
1.3. Installation de Kubernetes
Minikube : Idéal pour débuter avec Kubernetes en local. Il crée un cluster à nœud unique.
bash
Copy code
minikube start
kubectl : Outil en ligne de commande pour interagir avec un cluster Kubernetes.
bash
Copy code
kubectl get nodes
1.4. Première application sur Kubernetes
Créer un Pod :

yaml
Copy code
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  containers:
    - name: nginx-container
      image: nginx
Commande pour créer le Pod :

bash
Copy code
kubectl apply -f pod.yaml
Lister les Pods :

bash
Copy code
kubectl get pods
Niveau 2 : Intermédiaire
2.1. Services et exposition des Pods
Un Service permet de rendre un Pod accessible aux autres Pods ou à l'extérieur du cluster. Il existe plusieurs types de Services :

ClusterIP (par défaut) : Accès interne dans le cluster.
NodePort : Ouvre un port sur chaque nœud pour accéder au Pod.
LoadBalancer : Expose un service externe via un équilibreur de charge.
Exemple d’un service NodePort :

yaml
Copy code
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30007
  type: NodePort
2.2. ReplicaSets et Deployments
ReplicaSet : Assure qu'un nombre spécifié de répliques de Pods sont en cours d'exécution.
Deployment : Gère la mise à jour et le déploiement de ReplicaSets.
Exemple de Deployment :

yaml
Copy code
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
Déployer l’application :

bash
Copy code
kubectl apply -f deployment.yaml
2.3. Namespaces
Les namespaces permettent de séparer les ressources au sein du cluster :

Créer un namespace :
bash
Copy code
kubectl create namespace mon-namespace
Déployer dans un namespace spécifique :
bash
Copy code
kubectl apply -f pod.yaml --namespace=mon-namespace
Niveau 3 : Avancé
3.1. ConfigMaps et Secrets
ConfigMap : Stocke des configurations non sensibles.
Secret : Stocke des données sensibles comme des mots de passe ou des clés API.
Exemple de ConfigMap :

yaml
Copy code
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  config_key: config_value
Exemple de Secret :

yaml
Copy code
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
data:
  password: cGFzc3dvcmQ=
3.2. Volumes et stockage
Kubernetes offre plusieurs options de stockage pour les Pods :

emptyDir : Stockage éphémère.
hostPath : Utilise un répertoire de l'hôte.
PersistentVolume (PV) et PersistentVolumeClaim (PVC) : Pour un stockage persistant.
Exemple d'un PVC :

yaml
Copy code
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-example
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
3.3. Health Checks : Liveness et Readiness Probes
Liveness probe : Vérifie si le conteneur doit être redémarré.
Readiness probe : Vérifie si le conteneur est prêt à recevoir du trafic.
Exemple de probe :

yaml
Copy code
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 3
  periodSeconds: 3
3.4. Horizontal Pod Autoscaling
L’autoscaler horizontal ajuste dynamiquement le nombre de Pods en fonction de la charge (CPU, RAM).

bash
Copy code
kubectl autoscale deployment nginx-deployment --cpu-percent=50 --min=1 --max=5
Niveau 4 : Expert
4.1. Kubernetes Ingress
L’Ingress permet de gérer l'accès HTTP/HTTPS aux services depuis l'extérieur du cluster. Exemple d'Ingress :

yaml
Copy code
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
spec:
  rules:
    - host: example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: nginx-service
                port:
                  number: 80
4.2. Helm : Gestionnaire de packages Kubernetes
Helm simplifie la gestion d’applications Kubernetes à travers des packages appelés Charts.

Installation d'un Chart Helm :
bash
Copy code
helm install mon-app stable/nginx
4.3. Monitoring et Logging
Prometheus et Grafana : Pour surveiller les performances des clusters.
ELK Stack (Elasticsearch, Logstash, Kibana) : Pour la collecte et l’analyse des logs des Pods.
4.4. CI/CD avec Kubernetes
Intégration des pipelines CI/CD pour automatiser le déploiement d'applications dans Kubernetes avec des outils comme :

Jenkins avec Kubernetes Plugin.
GitLab CI/CD et ArgoCD pour des déploiements GitOps.
4.5. Sécurité dans Kubernetes
Utiliser RBAC (Role-Based Access Control) pour gérer les autorisations.
Scanner les images pour les vulnérabilités.
Utiliser des Pod Security Policies pour renforcer la sécurité.
Conclusion
Ce parcours Kubernetes de débutant à expert vous guide à travers l'installation, la gestion des Pods et des Services, jusqu'à des concepts avancés comme l'autoscaling, l'ingress, et la sécurité des clusters. Kubernetes est une technologie complexe mais extrêmement puissante, essentielle pour la gestion d'applications conteneurisées à grande échelle.

Si vous avez des questions ou besoin d’approfondir certaines parties, faites-le-moi savoir !
