import { useState, useEffect } from "react"
import { BarChart, Bar, XAxis, YAxis } from "recharts"

function App() {
  const [scores, setScores] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/scores")
      .then(res => res.json())
      .then(data => setScores(data))
  }, [])

  const versionsTested = scores.length
  const accuracies = scores.map(row => row.correct / row.total * 100)
  const bestAccuracy = Math.max(...accuracies)
  const baselineRow = scores.find(row => row.version === "baseline")
  const baselineAccuracy = baselineRow ? (baselineRow.correct / baselineRow.total * 100) : 0
  const improvement = bestAccuracy - baselineAccuracy

  return (
    <div>
      <h1>My Dashboard</h1>
      <BarChart width={500} height={300} data={scores}>
        <XAxis dataKey="version" />
        <YAxis />
        <Bar dataKey="correct" fill="#1baf7a" />
      </BarChart>
    

    <div>
      <p> Version Tested</p>
      <p>{versionsTested}</p>
    </div>

    <div>
      <p>Best Accuracy</p>
      <p>{bestAccuracy.toFixed(1)}%</p>
    </div>
    <div>
      <p>Improvements</p>
      <p>{improvement.toFixed(1)}pts</p>
    </div>


  </div>
  )
}

export default App