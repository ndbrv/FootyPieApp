import "./Home.css";
import React, {useState} from 'react';
import { Chart } from "chart.js";
import ChartComp from "./ChartComp";

function Home() {

  const [playerName, setPlayerName] = useState("")
  const [playerStats, setPlayerStats] = useState({})
  const [loading, setLoading] = useState(true)
  const handleChange = e => {
    setPlayerName(e.target.value)
  }
  const baseURL = "http://localhost:5000/stats"
  const URL = baseURL + "/" + playerName
  const fetchData = () =>
    fetch(URL).then(response => response.json())

  const handleClick = () => 
     fetchData().then(data => {setPlayerStats(data)
     setLoading(false)})

 
  
    return (
      <div className="body-container">
        <h1 className="body-text"> Premier League Player Statistics </h1>
        <p>
          Enter a player's name to see their stats:
        </p>
        <div className="input-container">
          <input id="player-name" className="form-control form-control-lg" type="text" 
        value={playerName} placeholder="Player name..." onChange={handleChange}></input>
        <button className="btn btn-primary" type="submit" onClick={handleClick}> Submit </button>
        </div>
        <p>
          
        </p>
        <div className="chart-container">
          {loading ? "Loading" : <ChartComp data={playerStats}></ChartComp>}
        </div>
      </div>
    );
  }

  export default Home;