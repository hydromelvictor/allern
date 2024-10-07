# REACT

framework pour le front composé de HTML + CSS + JS

```bash
# creer un projet react
npx create-react-app projectname
```

## structure du projet

* node_modules/ (les dependances)
* public/ (ou se trouve le index.html)
  * index.html
* src/ (la ou nous devons travaller)
  * index.js (initialisation du projet)
* package.json (gestion des dependances)

├── README.md
├── node_modules
...
├── package.json
├── public
...
├── src
│   ├── index.js
│   ├── components
│   └── pages
│       └── Home
│            └── index.jsx


## Apprendre

```javascript

/* ==construire des listes avec map()== */
const numbers = [1, 2, 3, 4]
const doubles = numbers.map(x => x * 2) // [2, 4, 6, 8]

const plantList = [
    'monstera',
    'ficus lyrata',
    'pothos argenté',
    'yucca',
    'palmier'
]

function ShoppingList() {
    return (
        <ul>
            {plantList.map((plant, index) => (
                <li key={`${plant}-${index}`}>{ plant }</li>
            ))}
        </ul>
    )
}

export default ShoppingList


/*  utiliser le ternaire */
{
    name: 'monstera',
    category: 'classique',
    id: '1ed',
    isBestSale: true
},

{plantList.map((plant) => (
    <li key={ plant.id }>
        {plant.isBestSale ? <span>🔥</span> : <span>👎</span>}
    </li>
))}

```

## Réutilisez vos composants avec les props

```javascript

function CareScale(props) {
    const scaleValue = props.scaleValue
    return <div>{scaleValue}☀️</div>
}

export default CareScale


function CareScale(props) {
    const scaleValue = props.scaleValue

    const range = [1, 2, 3]

    return (
        <div>
            {range.map((rangeElem) =>
                scaleValue >= rangeElem ? <span key={rangeElem.toString()}>☀️</span> : null
            )}
        </div>
    )
}


function CareScale({ scaleValue, careType }) {
    const range = [1, 2, 3]
    
    const scaleType = careType === 'light' ? '☀️' : '💧'

    return (
        <div>
            {range.map((rangeElem) => scaleValue >= rangeElem ? <span key={rangeElem.toString()}>{scaleType}</span> : null
            )}
        </div>
    )
}


/* utilisation des props */
<CareScale careType='water' scaleValue={plant.water} />
<CareScale careType='light' scaleValue={plant.light} />


function Banner({ children }) {
    return <div className='lmj-banner'>{children}</div>
}


<Banner>
    <img src={logo} alt='La maison jungle' />
    <h1 className='lmj-title'>La maison jungle</h1>
</Banner>
```

## les evenements

```javascript

function handleClick() {
    console.log('✨ Ceci est un clic ✨')
}

function handleClick(plantName) {
    alert(`Vous voulez acheter 1 ${plantName} ? Très bon choix 🌱✨`)
}

<li className='lmj-plant-item' onClick={handleClick}>
    <img className='lmj-plant-item-cover' src={cover} alt={`${name} cover`} />
    {name}
    <div>
        <CareScale careType='water' scaleValue={water} />
        <CareScale careType='light' scaleValue={light} />
    </div>
</li>


function handleClick(plantName) {
    alert(`Vous voulez acheter 1 ${plantName} ? Très bon choix 🌱✨`)
}

/* si des parametres sont necessaire */
onClick={() => handleClick(name)}



function handleSubmit(e) {
    e.preventDefault()
    alert(e.target['my_input'].value)
}

<form onSubmit={handleSubmit}>
    <input type='text' name='my_input' defaultValue='Tapez votre texte' />
    <button type='submit'>Entrer</button>
</form>


/* changer les valeur des variable avec useState*/

import { useState } from 'react'

function QuestionForm() {
    const [inputValue, setInputValue] = useState('Posez votre question ici')
    return (
        <div>
            <textarea
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
            />
            <button onClick={() => alert(inputValue)}>Alertez moi 🚨</button>
        </div>
    )
}


export default QuestionForm

function checkValue(value) {
    if (!value.includes('f')) {
        setInputValue(value)
    }
}
```

## permettre a l'utilisateur d'interagir avec les données

```javascript

function Cart() {
    const monsteraPrice = 8
    const [cart, updateCart] = useState(0)

    return (
        <div className='lmj-cart'>
            <h2>Panier</h2>
            <div>
                Monstera : {monsteraPrice}€
                <button onClick={() => updateCart(cart + 1)}>
                    Ajouter
                </button>
            </div>
            <h3>Total : {monsteraPrice * cart}€</h3>
        </div>
    )
}



function Cart() {
    const monsteraPrice = 8
    const [cart, updateCart] = useState(0)
    const [isOpen, setIsOpen] = useState(false)
 
    return isOpen ? (
        <div className='lmj-cart'>
            <button onClick={() => setIsOpen(false)}>Fermer</button>
            <h2>Panier</h2>
            <div>
                Monstera : {monsteraPrice}€
                <button onClick={() => updateCart(cart + 1)}>
                    Ajouter
                </button>
            </div>
            <h3>Total : {monsteraPrice * cart}€</h3>
        </div>
    ) : (
        <button onClick={() => setIsOpen(true)}>Ouvrir le Panier</button>
    )
}


/* partager les states entre differents composant */

function App() {
    const [cart, updateCart] = useState([])
    
    return (
        <div>
            <Banner>
                <img src={logo} alt='La maison jungle' className='lmj-logo' />
                <h1 className='lmj-title'>La maison jungle</h1>
            </Banner>
            <div className='lmj-layout-inner'>
                <Cart cart={cart} updateCart={updateCart} />
                <ShoppingList cart={cart} updateCart={updateCart} />
            </div>
            <Footer />
        </div>
    )
}

export default App


function Cart({ cart, updateCart }) {
    const monsteraPrice = 8
    const [isOpen, setIsOpen] = useState(true)

    return isOpen ? (
        <div className='lmj-cart'>
            <button
                className='lmj-cart-toggle-button'
                onClick={() => setIsOpen(false)}
            >
                Fermer
            </button>
            <h2>Panier</h2>
            <h3>Total : {monsteraPrice * cart}€</h3>
            <button onClick={() => updateCart(0)}>Vider le panier</button>
        </div>
    ) : (
        <div className='lmj-cart-closed'>
            <button
                className='lmj-cart-toggle-button'
                onClick={() => setIsOpen(true)}
            >
                Ouvrir le Panier
            </button>
        </div>
    )
}

export default Cart



function ShoppingList({ cart, updateCart }) {
// Petite précision : categories nous vient de la partie précédente pour récupérer toutes les catégories uniques de plantes.

    const categories = plantList.reduce(
        (acc, elem) =>
            acc.includes(elem.category) ? acc : acc.concat(elem.category),
            []
    )
    
    return (
        <div className='lmj-shopping-list'>
            <ul>
                {categories.map((cat) => (
                <li key={cat}>{cat}</li>
                ))}
            </ul>
            <ul className='lmj-plant-list'>
                {plantList.map(({ id, cover, name, water, light }) => (
                    <div key={id}>
                        <PlantItem cover={cover} name={name} water={water} light={light} />
                        <button onClick={() => updateCart(cart + 1)}>Ajouter</button>
                    </div>
                ))}
            </ul>
        </div>
    )
}

export default ShoppingList
```

## Déclenchez des effets avec useEffect

Mais comment faire si on veut effectuer une action qui ne fait pas partie du return ? Qui intervient après que React a mis à jour le DOM ? Par exemple, si vous voulez déclencher une alerte à chaque fois que votre panier est mis à jour ? Ou bien même pour sauvegarder ce panier à chaque mise à jour ?

```javascript

import { useState, useEffect } from 'react'


function Cart({ cart, updateCart }) {
    const [isOpen, setIsOpen] = useState(true)
    const total = cart.reduce(
        (acc, plantType) => acc + plantType.amount * plantType.price,
            0
        )
    useEffect(() => {
        alert(`J'aurai ${total}€ à payer 💸`)
    }, [])

    return isOpen ? (
        <div className='lmj-cart'>
            <button
                className='lmj-cart-toggle-button'
                onClick={() => setIsOpen(false)}
            >
                Fermer
            </button>
            {cart.length > 0 ? (
                <div>
                    <h2>Panier</h2>
                    <ul>
                        {cart.map(({ name, price, amount }, index) => (
                            <div key={`${name}-${index}`}>
                                    {name} {price}€ x {amount}
                            </div>
                        ))}
                    </ul>
                    <h3>Total :{total}€</h3>
                    <button onClick={() => updateCart([])}>Vider le panier</button>
                </div>
            ) : (
                <div>Votre panier est vide</div>
            )}
        </div>
    ) : (
        <div className='lmj-cart-closed'>
            <button
                className='lmj-cart-toggle-button'
                onClick={() => setIsOpen(true)}
            >
                Ouvrir le Panier
            </button>
        </div>
    )
}


/*Dans notre cas, si je veux que l'alerte ne s'affiche que lorsque le total de mon panier change, il me suffit de faire : */

useEffect(() => {
    alert(`J'aurai ${total}€ à payer 💸`)
}, [total])

/*
Appelez toujours  useEffect   à la racine de votre composant. Vous ne pouvez pas l'appeler à l’intérieur de boucles, de code conditionnel ou de fonctions imbriquées. Ainsi, vous vous assurez d'éviter des erreurs involontaires.

Comme pour  useState,  useEffect   est uniquement accessible dans un composant fonction React. Donc ce n'est pas possible de l'utiliser dans un composant classe, ou dans une simple fonction JavaScript.
*/
```

## routage

```javascript

import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Home from './pages/Home/'
import Survey from './pages/Survey/'

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/survey/:questionNumber" element={<Survey />} />
        <Route path="*" element={<Error />} />
      </Routes>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
)
```

## les liens

```javascript

import { Link } from 'react-router-dom'

function Header() {
    return (
        <nav>
            <Link to="/">Accueil</Link>
            <Link to="/survey/42">Questionnaire</Link>
        </nav>
    )
}

export default Header

/*  utiliser les useParams pour recuperer le parametre dans la survey */
import { useParams } from 'react-router-dom'
 
function Survey() {
    const { questionNumber } = useParams()
 
    return (
        <div>
            <h1>Questionnaire 🧮</h1>
            <h2>Question {questionNumber}</h2>
        </div>
    )
}
```

## les Outlets

```javascript

import { Outlet, Link } from 'react-router'

function Survey() {
  return (
    <div>
      <h1>Questionnaire 🧮</h1>
      <Link to="client">Questionnaire Client</Link>
      <Link to="freelance">Questionnaire Freelance</Link>
      <Outlet />
    </div>
  )
}
export default Survey



import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Home from './pages/Home/'
import Survey from './pages/Survey/'
import Header from './components/Header'
// On ajoute nos composants
import ClientForm from './components/ClientForm'
import FreelanceForm from './components/FreelanceForm'

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/survey" element={<Survey />}>
          { /* Nous imbriquons nos composants dans survey */}
          <Route path="client" element={<ClientForm />} />
          <Route path="freelance" element={<FreelanceForm />} />
        </Route>
      </Routes>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
)

```

## Créez une route pour les attraper toutes : 404

```javascript
function Error() {
    return (
        <div>
            <h1>Oups 🙈 Cette page n'existe pas</h1>
        </div>
    )
}
 
export default Error
```

## Indiquez les types de vos props avec les PropTypes

```bash

# installer prop-types
npm add prop-types
```

```javascript

import PropTypes from 'prop-types'
 
function Card({ label, title, picture }) {
    return (
        <div style={{ display: 'flex', flexDirection: 'column', padding: 15 }}>
            <span>{label}</span>
            <img src={picture} alt="freelance" height={80} width={80} />
            <span>{title}</span>
        </div>
    )
}
 
Card.propTypes = {
    label: PropTypes.string,
    title: PropTypes.string,
    picture: PropTypes.string,
}
 
export default Card

/* definis une prop comme obligatoire*/
Card.propTypes = {
    label: PropTypes.string,
    title: PropTypes.string.isRequired,
    picture: PropTypes.string
}

/* definis des props par defaut*/
Card.defaultProps = {
    title: 'Mon titre par défaut',
}
```

## styled

```bash
npm add styled-components
```

```javascript

import styled from 'styled-components'

const CardLabel = styled.span``
```

## Passez des props dans votre CSS

```javascript

const StyledLink = styled(Link)`
    padding: 15px;
    color: #8186a0;
    text-decoration: none;
    font-size: 18px;
    ${(props) =>
        props.$isFullLink &&
        `color: white; border-radius: 30px; background-color: #5843E4;`}
`

<StyledLink to="/survey/1" $isFullLink>
    Faire le test
</StyledLink>



const colors = {
    primary: '#5843E4',
    secondary: '#8186A0',
    backgroundLight: '#F9F9FC',
}

export default colors


const StyledLink = styled(Link)`
    padding: 15px;
    color: #8186a0;
    text-decoration: none;
    font-size: 18px;
    ${(props) =>
        props.$isFullLink &&
        `color: white; border-radius: 30px; background-color: ${colors.primary};`}
`


import colors from './colors'
import styled, { keyframes } from 'styled-components'
 
const rotate = keyframes`
    from {
        transform: rotate(0deg);
    }
 
    to {
    transform: rotate(360deg);
    }
`
 
export const Loader = styled.div`
    padding: 10px;
    border: 6px solid ${colors.primary};
    border-bottom-color: transparent;
    border-radius: 22px;
    animation: ${rotate} 1s infinite linear;
    height: 0;
    width: 0;
`
```

## Créez un style global

```javascript

const GlobalStyle = createGlobalStyle`
    div {
        font-family: 'Trebuchet MS', Helvetica, sans-serif;
    }
`

/* Et vous l'importez tout simplement dans vos composants */

<Router>
    <GlobalStyle />
    <Header />
        …
</Router>
```

## userEffect

useEffect  est également un hook, qui permet d'exécuter des actions après le render de nos composants, en choisissant à quel moment et à quelle fréquence cette action doit être exécutée, avec le tableau de dépendances.

Vous vous en doutez sûrement, nous allons les utiliser pour faire des calls API :

useEffect  nous permettra de déclencher le fetch;

useState  permettra de stocker le retour de l'API dans le  state  .

```javascript

/* recuperer des données */

useEffect(() => {
   fetch(`http://localhost:8000/survey`)
        .then((response) => response.json()
        .then(({ surveyData }) => console.log(surveyData))
        .catch((error) => console.log(error))
    )
}, [])



function Survey() {
    const { questionNumber } = useParams()
    const questionNumberInt = parseInt(questionNumber)
    const prevQuestionNumber = questionNumberInt === 1 ? 1 : questionNumberInt - 1
    const nextQuestionNumber = questionNumberInt + 1
    const [surveyData, setSurveyData] = useState({})
 
    useEffect(() => {
        setDataLoading(true)
        fetch(`http://localhost:8000/survey`)
            .then((response) => response.json()
            .then(({ surveyData }) => console.log(surveyData))
            .catch((error) => console.log(error))
        )
    }, [])
 
    return (
        <SurveyContainer>
            <QuestionTitle>Question {questionNumber}</QuestionTitle>
            <QuestionContent>{surveyData[questionNumber]}   </QuestionContent>
            <LinkWrapper>
                <Link to={`/survey/${prevQuestionNumber}`}>Précédent</Link>
                {surveyData[questionNumberInt + 1] ? (
                    <Link to={`/survey/${nextQuestionNumber}`}>Suivant</Link>
                ) : (
                    <Link to="/results">Résultats</Link>
                )}
            </LinkWrapper>
        </SurveyContainer>
    )
}
 
export default Survey

```

## Partagez vos données avec le Contexte et useContext

 Contexte nous permet de récupérer simplement nos datas sans avoir à tout passer manuellement. Pour cela, on englobe le composant parent le plus haut dans l’arborescence de composants avec ce qu’on appelle un Provider  . Tous les composants enfants pourront alors se connecter au Provider  (littéralement en anglais, le “fournisseur”) et ainsi accéder aux props, sans avoir à passer par tous les composants intermédiaires. On dit que les composants enfants sont les Consumers  (consommateurs).

```javascript

import { createContext } from "react";

export const ThemeContext = createContext()


export const ThemeProvider = ({ children }) => {
    const [theme, setTheme] = useState('light')
    const toggleTheme = () => {
        setTheme(theme === 'light' ? 'dark' : 'light')
    }
 
    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    )
}



ReactDOM.render(
  <React.StrictMode>
    <Router>
      <ThemeProvider>
        <GlobalStyle />
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/survey/:questionNumber" element={<Survey />} />
          <Route path="/results" element={<Results />} />
          <Route path="/freelances" element={<Freelances />} />
          <Route path="*" element={<Error />} />
        </Routes>
        <Footer />
      </ThemeProvider>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);




import { useContext } from 'react'
import { ThemeContext } from '../context/ThemeProvider'

function GlobalStyle() {
    const { theme } = useContext(ThemeContext)

    return <StyledGlobalStyle isDarkMode={theme === 'dark'} />
}


const StyledGlobalStyle = createGlobalStyle`
    * {
        font-family: 'Trebuchet MS', Helvetica, sans-serif;
    }
 
    body {
        background-color: ${({ isDarkMode }) => (isDarkMode ? 'black' : 'white')};
        margin: 0;  
    }
`



const { toggleTheme, theme } = useContext(ThemeContext)

function Footer() {
    const { toggleTheme, theme } = useContext(ThemeContext)
    return (
        <FooterContainer>
        <NightModeButton onClick={() => toggleTheme()}>
            Changer de mode : {theme === 'light' ? '☀️' : '🌙'}
        </NightModeButton>
        </FooterContainer>
    )
}
```

## Allez plus loin avec les hooks

### Créez un hook pour vos calls API

```javascript


import { useState, useEffect } from 'react'

 

export function useFetch(url) {

    const [data, setData] = useState({})
    const [isLoading, setLoading] = useState(true)

    useEffect(() => {
        if (!url) return setLoading(True)


async function fetchData() {
                const response = await fetch(url)
                const data = await response.json()
                setData(data)
                setLoading(false)
            }

            setLoading(true)
            fetchData()
    }, [url])

    return { isLoading, data }

}



import { useFetch } from '../utils/hooks'

const { data, isLoading } = useFetch(`http://localhost:8000/survey`)
const { surveyData } = data

<QuestionContent>
    {surveyData && surveyData[questionNumber]}
</QuestionContent>
```

## Découvrez la base des tests dans React avec Jest

```javascript

/* index.test.js */

import { formatJobList } from './'
 
test('Ceci est mon premier test', () => {
    const expectedState = 'item2,'
    expect(formatJobList('item2', 3, 1)).toEqual(expectedState)
})

npm run test

/* englobé plusieurs test*/
import { formatJobList } from './'
 
describe('La fonction formatJobList', () => {
    test('ajoute une virgule à un item', () => {
        const expectedState = 'item2,'
        expect(formatJobList('item2', 3, 1)).toEqual(expectedState)
    })
    test('ne met pas de virgule pour le dernier élément', () => {
        const expectedState = 'item3'
        expect(formatJobList('item3', 3, 2)).toEqual(expectedState)
    })
})
```

## Assurez-vous d'avoir le test coverage idéal

Lorsqu’on commence à avoir des tests, il devient possible de mesurer la couverture de tests (code coverage), c’est-à-dire le pourcentage de notre code – à l’expression près ! – qui est couvert par les tests. On peut alors repérer les parties non testées, ou insuffisamment testées, et savoir ainsi où concentrer nos prochains efforts d’écriture de tests.

Lançons dès maintenant la commande nous permettant de vérifier notre code coverage.

Pour cela, je fais  npm test -- --coverage  .

## Testez vos composants avec React Testing Library

```javascript

import Footer from './'
import { render } from '@testing-library/react'
 
describe('Footer', () => {
    test('Should render without crash', async () => {
        render(<Footer />;)
    })
})


import Footer from './'
import { render } from '@testing-library/react'
import { ThemeProvider } from '../../utils/context'

describe('Footer', () => {
    test('Should render without crashing', async () => {
        render(
            <ThemeProvider>
                <Footer />
            </ThemeProvider>
        )
    })
})


test('Change theme', async () => {
    render(
        <ThemeProvider>
            <Footer />
        </ThemeProvider>
    )
    const nightModeButton = screen.getByRole('button')
})


test('Change theme', async () => {
    render(
        <ThemeProvider>
            <Footer />
        </ThemeProvider>
    )
    const nightModeButton = screen.getByRole('button')
    expect(nightModeButton.textContent).toBe('Changer de mode : ☀️')
})


import { render, screen, fireEvent } from '@testing-library/react'
import { ThemeProvider } from '../../utils/context'
import Footer from './'
 
test('Change theme', async () => {
    render(
        <ThemeProvider>
            <Footer />
        </ThemeProvider>
    )
    const nightModeButton = screen.getByRole('button')
    expect(nightModeButton.textContent).toBe('Changer de mode : ☀️')
    fireEvent.click(nightModeButton)
    expect(nightModeButton.textContent).toBe('Changer de mode : 🌙')
})
```

## Testez des composants qui font des calls API

Installez msw  pour faire vos simulations de calls API
Pour pouvoir simuler nos calls API, un peu de configuration s'impose à nous. Si, comme moi, vous n'aimez pas la config, ne vous inquiétez pas : je vous promets que ça ne durera pas trop longtemps !

Pour faire nos mocks, React Testing Library recommande d'utiliser une bibliothèque externe : MSW (pour Mock Service Worker), hébergée sur GitHub. On commence donc par installer la bibliothèque :

npm add msw --dev

## creer des mocks

```javascript

import { rest } from 'msw'
import { setupServer } from 'msw/node'
import { render, waitFor, screen } from '@testing-library/react'
 
import Freelances from './'
 
const server = setupServer(
    // On précise ici l'url qu'il faudra "intercepter"
    rest.get('http://localhost:8000/freelances', (req, res, ctx) => {
        // Là on va pouvoir passer les datas mockées dans ce qui est retourné en json
        return res(ctx.json({}))
    })
)
 
// Active la simulation d'API avant les tests depuis server
beforeAll(() => server.listen())
// Réinitialise tout ce qu'on aurait pu ajouter en termes de durée pour nos tests avant chaque test
afterEach(() => server.resetHandlers())
// Ferme la simulation d'API une fois que les tests sont finis
afterAll(() => server.close())



const freelancersMockedData = [
    {
        name: 'Harry Potter',
        job: 'Magicien frontend',
        picture: '',
    },
    {
        name: 'Hermione Granger',
        job: 'Magicienne fullstack',
        picture: '',
    },
]

const server = setupServer(
    // On précise ici l'url qu'il faudra "intercepter"
    rest.get('http://localhost:8000/freelances', (req, res, ctx) => {
        // Là on va pouvoir passer les datas mockées dans ce qui est retourné en json
        return res(ctx.json({ freelancersList: freelancersMockedData }))
    })
)
```
