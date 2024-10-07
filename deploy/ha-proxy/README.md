# HA-proxy

HAProxy est un relais TCP/HTTP offrant des facilités d'intégration en environnement hautement
disponible. En effet, il est capable :

* d'effectuer un aiguillage statique défini par des cookies ;
* d'effectuer une répartition de charge avec création de cookies pour assurer la persistance de session ;
* de fournir une visibilité externe de son état de santé ;
* de s'arrêter en douceur sans perte brutale de service ;
* de modifier/ajouter/supprimer des en-têtes dans la requête et la réponse ;
* d'interdire des requêtes qui vérifient certaines conditions ;
* d'utiliser des serveurs de secours lorsque les serveurs principaux sont hors d'usage.
* de maintenir des clients sur le bon serveur d'application en fonction de cookies applicatifs.
* fournir des rapports d'état en HTML à des utilisateurs authentifiés, à travers des URI de
l'application interceptées.

Il requiert peu de ressources, et son architecture événementielle mono-processus lui permet
facilement de gérer plusieurs milliers de connexions simultanées sur plusieurs relais sans effondrer le
système.
