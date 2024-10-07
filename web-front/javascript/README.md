# javascript

DOM (Document Object Model, modèle objet de document)

```javascript
for (let i = 0; i < 5; i++) { ... }

if (...) {
...
} else {
...
}

let add = function(a, b) {
    return a + b;
}

// For each loop
const groceries = ['milk', 'cocoa puffs'];
for (let item of groceries)
    console.log(item);

// Callback style
groceries.forEach(function(item) {
    console.log(item);
});

// Nerdy callback style (use that!)
groceries.forEach(item => {
    console.log(item);
});

```

## Window

```javascript
// afficher le nom du navigateur dans une alert
window.alert(navigator.appName);

// popup de confirmation
window.confirm('Do you really want to do this?')

// demande
let name = window.prompt("Enter your name!", "<Your name>")

// au chargement de la page
window.onload = function() {
    let img = new Array("active.gif", "inactive.gif", "other.gif");
    preloadImages(img);
}

//
window.setTimeout(func(), milliSecondTime)

// au scroll
window.onscroll = positionNavigation;

window.innerWidth
window.pageYOffset
window.pageXOffset

// Ferme la nouvelle fenêtre si la fenêtre parent est fermée
dependent
// Bascule la barre d'outils personnelle
directories
// Hauteur de la fenêtre
height
// Hauteur de la fenêtre, en excluant sa décoration (navigateurs sauf IE)
innerHeight
// Largeur de la fenêtre, en excluant sa décoration (navigateurs sauf IE)
innerWidth
// Position horizontale de la fenêtre (IE uniquement)
left
// Bascule la barre d'emplacement
location
// Bascule la barre de menus
menubar
// Hauteur de la fenêtre (navigateurs sauf IE)
outerHeight
// Largeur de la fenêtre (navigateurs sauf IE)
outerWidth
// Lorsque la fenêtre peut être redimensionnée par l'utilisateur
resizeable
// Position horizontale de la fenêtre (navigateurs sauf IE)
screenX
// Position verticale de la fenêtre(navigateurs sauf IE)
screenY
// Bascule les barres de défilement
scrollbars
// Bascule la barre d'état
status
// Bascule la barre d'outils
toolbar
// Position verticale de la fenêtre(IE uniquement)
top
// Largeur de la fenêtre
width
// Donne à la fenêtre une valeur z-lock(position de l'axe des z) inférieure
z-lock
//Centre la fenêtre
center
// Hauteur de la fenêtre
dialogHeight
// Position horizontale de la fenêtre
dialogLeft
// Position verticale de la fenêtre
dialogTop
// Largeur de la fenêtre
dialogWidth
// Bascule le symbole d'aide dans le coin supérieur droit
help
// Définit la largeur et la hauteur de la fenêtre sur les valeurs fournies, comme dans le code précédent (fichier resizeto.html dans l'archive de téléchargement).
resizeTo(). 
window.resizeTo(640, 480);

// Modifie la largeur et la hauteur de la fenêtre en ajoutant les valeurs fournies, comme le montre le listing suivant (qui réduit de moitié la largeur et la hauteur)
resizeBy()

// repositionner
window.moveBy(-10, 10);
// fermeture d'un femetre
if (!newwindow.closed) newwindow.close();


// ouvrir une nouvelle fenetre
window.open("http://www.samspublishing.com/", "samsWindow", "");
window.open("http://www.samspublishing.com/", "samsWindow", "width=640,height=480,directories=no,menubar=no, toolbar=no,scrollbars=yes");

// ouverture d'une fenetre modal
window.showModalDialog("http://www.samspublishing.com/","samsWindow", "dialogWidth=640,dialogHeight=480,status=no,center=yes");

```

### Historique du navigateur

```javascript
// page precedent
window.history.back();
// page suivante
window.history.forward();
```

## Document

```javascript
// creer un novelle element
document.createElement("div");

// creer un element de text
let newTextNode = document.createTextNode("Item " + nr);

// selectionner un element par 
// .1 id
document.getElementById("monId")
// .2 balise => sa sorti est un tableau
document.getElementsByTagName("p")
// .3 selecteur generale
document.querySelector('css selector')
document.querySelectorAll('css selector')

// action sur un element
let elt = document.getElementById("monId")
// .1 premier noeud enfant
elt.firstChild
// .2 dernier noeud enfant
elt.lastChild
// tous les noeud enfant
elt.childNodes
// noeud parent
elt.parentNode
// noeud suivant de meme niveau
elt.nextSibling
// noeud precedent de meme niveau
elt.previousSibling
// renvoie le nom de la balise du noeud
elt.nodeName
// sur les nouead de text et renvoie le text
elt.nodeValue
// type du neaud
elt.nodeType
// suppression d'element
elt.removeChild(elt.lastChild);
elt.remove();
// ajout de element
elt.appendChild(newNode);
// ajout avant un element precis
elt.insertBefore(newNode, elt.firstChild);
// cloner un element existant
newItem = oldItem.cloneNode(true);
// remplacer un element
elt.replaceChild(newNode, list.firstChild);
// ecrit le code html dans l'element
let newNode = "<li>Item " + nr + "</li>";
list.innerHTML += newNode;


// => les attributs <==
// ajouter un lien
newLink.setAttribute("href","http://www.samspublishing.com/");


// creer un nombre aleatoire
let rand = min + Math.floor((max – min + 1) * Math.random())

// derniere modification de la page
document.write(document.lastModified);

// accedez aux feuille de style et les desactiver ou activer
document.styleSheets[0].disabled = true;
document.styleSheets[0].disabled = false;
```

## Location

```javascript
// redirection du navigateur a une autre page
location.href = "newPage.html"

// rechargement de la page
location.reload();

// recuperation des parametre GET
let ls = location.search.substring(1);
let namevalue = ls.split("&");
```

## les expressions regulieres

```javascript
// Début de la chaîne
^
// Fin de la chaîne
$
// 0 ou 1 fois (fait référence au caractère ou à l'expression précédent)
?
// 0 fois ou plus (fait référence au caractère ou à l'expression précédent)
*
//1 ou plusieurs fois (fait référence au caractère ou à l'expression précédent)
+
// Caractères alternatifs
[...]
// (utilisé entre crochets)
-
//(utilisé entre crochets)
^
// Une suite de valeurs Correspond à tout sauf aux caractères suivants Motifs alternatifs
|
// Définit un sous-motif
(...)
// quel Nombre minimal et maximal d'occurrences ; si min ou max est omis, cela signifie 0 ou infinite
{min,max}
// N'importecaractère
.
// Echappement du caractère suivant
\

// definir une expression reguliere

let zip = new RegEx("\\d{5}");
let zip = /\d{5}/;

// La méthode match() renvoie toutes les correspondances ;
// exec() ne renvoie que l'expression courante, généralement la première.
let matches = zip.exec("Indianapolis, IN 46240");

let address = /(\w+), ([A-Z]{2}) (\d{5})/;
let sams = "Indianapolis, IN 46240";
let result = sams.replace(address, "$3 $1, $2");

```

## Les dates

```javascript
// date
let d = new Date();
// Jour du mois
getDate()
// Année à quatre chiffres
getFullYear()
// Heures
getHours()
// Minutes
getMinutes()
// Mois moins 1 (!)
getMonth()
// Secondes
getSeconds()
//  Valeur "epoch" (date de début de mesure du temps sur un système d'exploitation)
getTime()
// Représentation en chaîne
toString()
// Représentation en chaîne UTC
toUTCString()
```

## Images

```javascript
let i = new Image();
i.src = "";
```

## les tableaux

```javascript
let img = new Array();
```

## Styles de curseur CSS

Voici les valeurs autorisées pour la propriété cursor de JavaScript/CSS :

* auto
* crosshair
* default
* e-resize
* help
* move
* n-resize
* ne-resize
* nw-resize
* pointer
* s-resize
* se-resize
* sw-resize
* test
* w-resize
* wait

```javascript
// ajouter un style
document.getElementById("para").style.fontWeight ="strong";
// ajouter une classe
document.getElementById("para").className = "strong";
```

## Les classes

```javascript
// creer un class
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    displayAge() {
        console.log(this.age);
    }

    displayName() {
        console.log(this.age);
    }

    displayAgeAndName() {
        this.displayAge();
        this.displayName();
    }
}

const p = new Person("Joe",1);

// Heritage
/* ce qui signifie que UniversalCounter heritera des function de UniversalTranslator*/
UniversalCounter.prototype = new UniversalTranslator();

/* de meme isLeapYear deviendra un eleme de date (Date.isLeapYear)*/
Date.prototype.isLeapYear = isLeapYear;

```

## Evenement

```javascript
// l'événement sera intercepté lors de sa descente (true) ou lors de sa remontée (false).
/* l'evenement descend vers la cible puis remonte a la surface */
button.addEventListener("click", eventHandler, false);
// apres interception on peut stopper sa circulation
e.stopPropagation();
button.removeEventListener()

// evenement de clavier
document.onkeydown = showKey;

// evenement de la souris
/* 0=button gauche, 1=button median, 2=button droit */
document.onmousemove = showPosition;
```

## Cookies

```javascript
// definir un cookie
document.cookie = "myLanguage=JavaScript";
// lire un cookie
let cookies = document.cookie.split(/; /g);
/*
1. Séparer la chaîne de cookie à "; " (pour obtenir des
cookies individuels).
2. Identifier le premier signe égal (=) dans chaque cookie
comme délimiteur de valeur et de nom.
*/
let cookies = document.cookie.split(/; /g);
for (var i=0; i<cookies.length; i++) {
    let cookie = cookies[i];
    if (cookie.indexOf("=") == -1) {
        continue;
    }
    let name = cookie.substring(0, cookie.indexOf("="));
    let value = cookie.substring(cookie.indexOf("=") + 1);
    document.write("<tr><td>" + HtmlEscape(name) + "</td><td>" + HtmlEscape(unescape(value)) + "</td></tr>");
}

function getCookie(name) {
    let pos = document.cookie.indexOf(name + "=");
    if (pos == -1) {
        return null;
    } else {
        let pos2 = document.cookie.indexOf(";", pos);
        if (pos2 == -1) {
            return unescape(
                document.cookie.substring(pos + name.length + 1));
        } else {
                return unescape(document.cookie.substring(pos + name.length + 1,pos2));
        }
    }
}

// etablir une date d'expiration
document.cookie="myLanguage=JavaScript; expires=Tue, 25-Dec-2007 12:34:56 GMT"
// suppression de cookie
document.cookie="myLanguage=JavaScript; expires=Thu, 25-Dec-1980 12:34:56 GMT"
```

## Les formulaires

```javascript
document.forms[0]
field.value = "<Enter data here>";
```

## les Promise

```javascript
// fetch est une promise
const promise = fetch('images.txt');
promise.then(onSuccess, onFail);
fetch(url, {
    method: 'GET|POST|PUT|DELETE',
    body: {},
    headers: {}
})
.then(res => {
    if (res.status === ok) {
        return res.status(200).json({})
    }
    else {}
})
.catch(err => res.stats(500).json({ msg: err }))
```
