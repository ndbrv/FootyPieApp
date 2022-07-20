import {
  Chart as ChartJS,
  RadialLinearScale,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js';
import { PolarArea } from 'react-chartjs-2';

ChartJS.register(RadialLinearScale, ArcElement, Tooltip, Legend);

function ChartComp(props) {
    const allData = props.data
    console.log(allData)
    const stats = []
    const percentiles = []
    const colors = []
    for (var key in allData) {
      if (key != "name") {
        stats.push(allData[key][0])
        percentiles.push(allData[key][1])
      }
    }

    for (let i = 0; i < percentiles.length; i++) {
      colors.push(`rgba(${255*(1-percentiles[i])},${255*percentiles[i]},0,1)`)
      
    }
    console.log(colors)
    console.log(percentiles)

    const data = {
  labels: ['Assists','Expected Assists','Dribbles Completed','Non-Penalty Goals','Non-Penalty Expected Goals',
  'Non Penalty Expected Goals + Expected Assists','Pass Completion','Passes Attempted','Progressive Carries','Progressive Passes','Progressive Passes Received', 'Shot Creating Actions', 'Shots Total', 'Touches']
  ,
  datasets: [
    {
      label: 'Percentile',
      data: percentiles,
      backgroundColor: colors,
      borderWidth: 1,
    },
    
  ],
  
};

    return <PolarArea data={data}></PolarArea>
}

export default ChartComp;