import './App.css';
import Navbar from './components/Navbar';
import Home from './components/Home';
import {BrowserRouter as Router, RouteProps, Route, Link} from 'react-router-dom';

//import {} from '@material-ui/core';



function App() {
  return (
   <Router>
    <Navbar>
    </Navbar>
    <Home>
      </Home>
   </Router>
  );
}





export default App;
