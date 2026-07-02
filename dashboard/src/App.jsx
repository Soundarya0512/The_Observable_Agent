import { useState, useEffect } from "react"
import { BarChart, Bar, XAxis, YAxis } from "recharts"

function App() {
  const [scores, setScores] = useState([])

  useEffect(() => {
    fetch("http://localhost:8000/scores")
      .then(res => res.json())
      .then(data => setScores(data))
  }, [])

  return (
    <div>
      <h1>My Dashboard</h1>
      <BarChart width={500} height={300} data={scores}>
        <XAxis dataKey="version" />
        <YAxis />
        <Bar dataKey="correct" fill="#1baf7a" />
      </BarChart>
    </div>
  )
}

export default App