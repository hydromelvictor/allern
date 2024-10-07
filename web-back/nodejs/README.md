# NodeJs

## Installez Node

```bash

# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

# download and install Node.js (you may need to restart the terminal)
nvm install 20

# verifies the right Node.js version is in the environment
node -v # should print `v20.17.0`

# verifies the right npm version is in the environment
npm -v # should print `10.8.2`
```

## Qu'est-ce que Node ?

Avant de commencer, vous pouvez initialiser un dépôt Git en exécutant git init depuis
votre dossier backend .
N'oubliez pas de créer un fichier .gitignore contenant la ligne node_modules
afin de ne pas envoyer ce  dossier  (qui deviendra volumineux) vers votre dépôt distant.

Si, contrairement à moi, vous créez le dépôt Git en premier, vous pourrez ajouter son URL
distant à la configuration du projet Node pendant l'étape suivante.

```bash
# creer votre dossier de travail
mkdir back && cd back
# initialiser le projet
npm init
# changer le point d'entree en server.js
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (back) back
version: (1.0.0) 
description: connexion systeme
entry point: (index.js) server.js
test command: 
git repository: 
keywords: 
author: 
license: (ISC) 
About to write to /home/hydromel/workspaces/dylov/jsdylov/sign/back/package.json:

{
  "name": "back",
  "version": "1.0.0",
  "description": "connexion systeme",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}


Is this OK? (yes)
```

## preparer son environement

```bash
# creer les fichier server.js app.js
touch server.js app.js
# verifier que tout pas bien en demarant le server node
node server
# installer nodemon afin de demarer le server avec pour un reload automatic
npm install -g nodemon
# demarer avec
nodemon server
# installer express
npm install express
# installer dotenv pour les varialble d'environement
npm install dotenv
# creer un fichier .env a la racine du projet dans back
touch .env
# base de donnees
# .1 mongo avec mongoose
npm install mongoose
# .2 installer mongoose-unique-validator pour les champ unique
npm install mongoose-unique-validator
# .3 installer bcrypt pour les mot de pas
npm install bcrypt
# .4 installer jsonwebtoken pour l'authentification par token
npm install jsonwebtoken
# configurer le middleware d'athentification
mkdir middlewares && cd middlewares
touch auth.js
# configurer multer pour uploader les fichier
npm install multer
touch multer-config.js
# creer le dossier models dans back
mkdir models && cd models
# creer un fichier pour un models
touch user.js account.js
# creer le dossier routes pour le routage dans back
mkdir routes && cd routes
touch user.js account.js
# creer le dossier controllers pour y mettre la logique metier
mkdir controllers && cd controllers
touch user.js account.js
```

```javascript
/* ===========================
  back/server.js 
============================== */

const http = require('http');
const app = require('./app');
require('dotenv').config()

// normalizePort renvoie un port valide, qu'il soit fourni sous la forme d'un numéro ou d'une chaîne
const normalizePort = val => {
  const port = parseInt(val, 10);

  if (isNaN(port)) {
    return val;
  }
  if (port >= 0) {
    return port;
  }
  return false;
};
const port = normalizePort(process.env.PORT || '3000');
app.set('port', port);

// recherche les différentes erreurs et les gère de manière appropriée. Elle est ensuite enregistrée dans le serveur
const errorHandler = error => {
  if (error.syscall !== 'listen') {
    throw error;
  }
  const address = server.address();
  const bind = typeof address === 'string' ? 'pipe ' + address : 'port: ' + port;
  switch (error.code) {
    case 'EACCES':
      console.error(bind + ' requires elevated privileges.');
      process.exit(1);
      break;
    case 'EADDRINUSE':
      console.error(bind + ' is already in use.');
      process.exit(1);
      break;
    default:
      throw error;
  }
};

const server = http.createServer(app);

server.on('error', errorHandler);
server.on('listening', () => {
  const address = server.address();
  const bind = typeof address === 'string' ? 'pipe ' + address : 'port ' + port;
  console.log('Listening on ' + bind);
});

server.listen(port, process.env.HOST, () => {
    logger.info(`Start Server http://${process.env.HOST}:${port}`)
});



/* ============================
 back/app.js 
=============================== */

const express = require('express');
const mongoose = require('mongoose');
const path = require('path');

const userRoutes = require('../routes/user');
const signRoutes = require('../routes/sign');


// connexion a la base de donnees
mongoose.connect('mongodb+srv://jimbob:<PASSWORD>@cluster0-pme76.mongodb.net/test?retryWrites=true&w=majority')
  .then(() => console.log('Connexion à MongoDB réussie !'))
  .catch(() => console.log('Connexion à MongoDB échouée !'));

const app = express();

app.use(express.json())

app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content, Accept, Content-Type, Authorization');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS');
  next();
});

app.use('/images', express.static(path.join(__dirname, 'images')));

app.use('/api/user', userRoutes)
app.use('/api/auth', signRoutes);

module.exports = app;


/* ===========================
  back/middlewares/auth.js
============================== */

const jwt = require('jsonwebtoken');
require('dotenv').config()
 
module.exports = (req, res, next) => {
   try {const uniqueValidator = require('mongoose-unique-validator');
       const token = req.headers.authorization.split(' ')[1];
       const decodedToken = jwt.verify(token, process.env.SECRETKEY);
       const userId = decodedToken.userId;
       req.auth = {
           userId: userId
       };
        next();
    } catch(error) {
       res.status(401).json({ error });
   }
};

/* ===========================
  back/middlewares/multer-config.js
============================== */

const multer = require('multer');

const MIME_TYPES = {
  'image/jpg': 'jpg',
  'image/jpeg': 'jpg',
  'image/png': 'png'
};

const storage = multer.diskStorage({
  destination: (req, file, callback) => {
    callback(null, 'images');
  },
  filename: (req, file, callback) => {
    const name = file.originalname.split(' ').join('_');
    const extension = MIME_TYPES[file.mimetype];
    callback(null, name + Date.now() + '.' + extension);
  }
});

module.exports = multer({storage: storage}).single('image');


/* ===========================
  back/models/user.js
============================== */

const mongoose = require('mongoose');
const uniqueValidator = require('mongoose-unique-validator');

const userSchema = mongoose.Schema({
  username: { type: String, required: true},
  firstname: { type: String },
  lastname: { type: String },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  bio: { type: String, required: true },
  imageUrl: { type: String, required: true }
});

userSchema.plugin(uniqueValidator);

module.exports = mongoose.model('User', thingSchema);


/* ===========================
  back/models/account.js
============================== */
const mongoose = require('mongoose');

const accountSchema = mongoose.Scheme({
  author: { type: mongoose.Schema.Type.ObjectId, ref: 'User', required: true},
  price: { type: Number, required: true }
})


/* ===========================
  back/routes/user.js
============================== */
const express = require('express');
const router = express.Router();

const auth = require('../middlewares/auth');
const multer = require('../middlewares/multer-config');
const userCtrl = require('../controllers/user');

// api/user/...
router.get('/', auth, userCtrl.getAllUser);
router.post('/', multer, userCtrl.createUser);
router.get('/:id', auth, userCtrl.getOneUser);
router.put('/:id', auth, multer, userCtrl.modifyUser);
router.delete('/:id', auth, userCtrl.deleteUser);

module.exports = router;

/* ===========================
  back/routes/account.js
============================== */
const express = require('express');
const router = express.Router();

...

/* ===========================
  back/controllers/user.js
============================== */
const User = require('../models/user');

const fs = require('fs');


exports.createUser = (req, res, next) => {
   const userObject = JSON.parse(req.body.user);
   const user = new User({
       ...thingObject,
       imageUrl: `${req.protocol}://${req.get('host')}/images/${req.file.filename}`
   });
 
   user.save()
   .then(() => { res.status(201).json({message: 'Objet enregistré !'})})
   .catch(error => { res.status(400).json( { error })})
};

exports.getOneUser = (req, res, next) => {
  User.findOne({
    _id: req.params.id
  }).then(
    (user) => {
      res.status(200).json(user);
    }
  ).catch(
    (error) => {
      res.status(404).json({
        error: error
      });
    }
  );
};

exports.modifyUser = (req, res, next) => {
   const userObject = req.file ? {
       ...JSON.parse(req.body.user),
       imageUrl: `${req.protocol}://${req.get('host')}/images/${req.file.filename}`
   } : { ...req.body };
 
   delete userObject._userId;
   User.findOne({_id: req.params.id})
       .then((user) => {
           if (user.userId != req.auth.userId) {
               res.status(401).json({ message : 'Not authorized'});
           } else {
               User.updateOne({ _id: req.params.id}, { ...userObject, _id: req.params.id})
               .then(() => res.status(200).json({message : 'Objet modifié!'}))
               .catch(error => res.status(401).json({ error }));
           }
       })
       .catch((error) => {
           res.status(400).json({ error });
       });
};

exports.deleteUser = (req, res, next) => {
   User.findOne({ _id: req.params.id})
       .then(user => {
           if (user.userId != req.auth.userId) {
               res.status(401).json({message: 'Not authorized'});
           } else {
               const filename = user.imageUrl.split('/images/')[1];
               fs.unlink(`images/${filename}`, () => {
                   User.deleteOne({_id: req.params.id})
                       .then(() => { res.status(200).json({message: 'Objet supprimé !'})})
                       .catch(error => res.status(401).json({ error }));
               });
           }
       })
       .catch( error => {
           res.status(500).json({ error });
       });
};

exports.getAllUser = (req, res, next) => {
  User.find().then(
    (users) => {
      res.status(200).json(users);
    }
  ).catch(
    (error) => {
      res.status(400).json({
        error: error
      });
    }
  );
};


/* ===========================
  back/controllers/sign.js
============================== */

const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');


const User = require('../models/User');

exports.signup = (req, res, next) => {
  bcrypt.hash(req.body.password, 10)
    .then(hash => {
      const user = new User({
        email: req.body.email,
        password: hash
      });
      user.save()
        .then(() => res.status(201).json({ message: 'Utilisateur créé !' }))
        .catch(error => res.status(400).json({ error }));
    })
    .catch(error => res.status(500).json({ error }));
};


exports.login = (req, res, next) => {
   User.findOne({ email: req.body.email })
       .then(user => {
           if (!user) {
               return res.status(401).json({ error: 'Utilisateur non trouvé !' });
           }
           bcrypt.compare(req.body.password, user.password)
               .then(valid => {
                   if (!valid) {
                       return res.status(401).json({ error: 'Mot de passe incorrect !' });
                   }
                   res.status(200).json({
                       userId: user._id,
                       token: jwt.sign(
                           { userId: user._id },
                           'RANDOM_TOKEN_SECRET',
                           { expiresIn: '24h' }
                       )
                   });
               })
               .catch(error => res.status(500).json({ error }));
       })
       .catch(error => res.status(500).json({ error }));
};

/* ===========================
  back/controllers/account.js
============================== */
...

```

## example

```javascript

app.use('/api/stuff', (req, res, next) => {
  const stuff = [
    {
      _id: 'oeihfzeoi',
      title: 'Mon premier objet',
      description: 'Les infos de mon premier objet',
      imageUrl: 'https://cdn.pixabay.com/photo/2019/06/11/18/56/camera-4267692_1280.jpg',
      price: 4900,_id: req.params.id,
      title: req.body.title,
      description: req.body.description,
      imageUrl: req.body.imageUrl,
      price: req.body.price,
      userId: req.body.userId
      userId: 'qsomihvqios',
    },
    {
      _id: 'oeihfzeomoihi',
      title: 'Mon deuxième objet',
      description: 'Les infos de mon deuxième objet',
      imageUrl: 'https://cdn.pixabay.com/photo/2019/06/11/18/56/camera-4267692_1280.jpg',
      price: 2900,
      userId: 'qsomihvqios',
    },
  ];
  res.status(200).json(stuff);
});

app.use((req, res, next) => {
  console.log('Requête reçue !');
  next();
});

app.use((req, res, next) => {
  res.json({ message: 'Votre requête a bien été reçue !' });
  next();
});

app.use((req, res, next) => {
  console.log('Réponse envoyée avec succès !');
});

```

## BodyParser

C’est une bibliothèque vous permettant de directement parser le corps d’une requête. Le résultat sera directement disponible dans l’objet request.
BodyParser est middleware.

```bash
npm install body-parser
```

```javascript
const bodyParser = require("body-parser")
// Content-type: application/json
app.use(bodyParser.json())
// Content-type: application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))


app.post("/products", (req, res) => {
  product = {
    name: req.body.name,
    price: req.body.price
  }
  res.json(product)
})

```

```bash
 npm install mongodb --save
```

```bash
# Desintaller un module local : aller dans le répertoire de npm
install :
npm uninstall nom_du_module
# Desintaller un module global :
npm uninstall -g nom_du_module
```
