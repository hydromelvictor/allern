# Le Responsive Web Design

Le Responsive Design (aussi nommé Responsive Web Design), désigne l’ensemble des méthodes et des techniques permettant d'utiliser efficacement un même site web sur tous les type d'appareils connectés. Un site conçu en « Responsive » pourra être consulté : sur smartphone, sur ordinateur, sur TV ou sur tablette. L’idée est de proposer une réorganisation dynamique du site en fonction de la largeur du terminal sur lequel il est consulté.

## es points de rupture

- Pour les smartphones première génération (portrait)
  - Le point de rupture se situe à 320 pixels
- Pour les smartphones première génération (paysage)
  - Le point de rupture se situe à 480 pixels
- Pour les petites tablettes ou le Kindle d'Amazon
  - Le point de rupture se situe à 600 pixels
- Pour les tablettes en mode portrait
  - Le point de rupture se situe à 768 pixels
- Pour les écrans de base et pour les tablettes en mode paysage
  - Le point de rupture se situe à 1024 pixels
- Pour les écrans plus larges, téléviseurs, etc
  - Le point de rupture se situe à 1200 pixels

```css
@media screen and (max-width: 600px) {
background: #000000;
}
```

Dans cet exemple, si le media est un écran et que la largeur maximale de sa zone d'affichage est 600px, alors sa couleur de
background sera le noir.

Une media query est une expression dont la valeur est toujours vraie ou fausse. Il suffit d'associer différentes déclarations possibles avec un opérateur logique pour définir un ensemble de conditions à réunir pour appliquer des styles CSS.
Les opérateurs logiques peuvent être :

- and : "et",
- only : "uniquement"
- not : "non".

Pour obtenir l'équivalent du "ou", il suffit d'énumérer différentes media queries à la suite, séparées par des virgules : si l'une d'entre elles est valable, alors l'ensemble de la règle sera appliquée.

```css
@media screen and (min-width: 600px) and (max-width: 900px) {
background: #000000;
}
```
