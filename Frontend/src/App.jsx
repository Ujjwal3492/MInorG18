import Card from "./Components/EVENTS/Card.jsx"
import Hero from "./Components/Heros/Hero.jsx"
import Navbar from "./Components/Navbar/Navbar.jsx"

/**
 * The main application component.
 * 
 * @returns {JSX.Element} The JSX element representing the application.
 */
function App() {
  return (
    <>
      <Navbar />
      <Hero />
      <Card />
    </>
  )
}

export default App;