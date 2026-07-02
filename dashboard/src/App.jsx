import { useState, useEffect } from "react"
import { BarChart, Bar, XAxis, YAxis,ResponsiveContainer  } from "recharts"
import "./App.css"

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
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>The Observable Agent</h1>
        <p className="subtitle">I kept asking "how do you know?" — so I built something that could answer.</p>
      </header>

      <div className="summary-row">
        <div className="card">
          <p className="card-label">Best Accuracy</p>
          <p className="card-value">{bestAccuracy.toFixed(1)}%</p>
        </div>
        <div className="card">
          <p className="card-label">Improvement</p>
          <p className="card-value">+{improvement.toFixed(1)} pts</p>
        </div>
        <div className="card">
          <p className="card-label">Versions Tested</p>
          <p className="card-value">{versionsTested}</p>
        </div>
      </div>

      <div className="chart-card">
        <p className="chart-title">Accuracy by Version</p>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={scores}>
            <XAxis dataKey="version" />
            <YAxis />
            <Bar dataKey="correct" fill="#8b5cf6" radius={[6, 6, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}

export default App
