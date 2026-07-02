import { useState, useEffect } from "react"

function App() {
  const [scores, setScores] = useState([])      // the board (empty at first)

  useEffect(() => {                             // when page loads...
    fetch("http://localhost:8000/scores")       // go to your backend
      .then(res => res.json())                  // unpack the response
      .then(data => setScores(data))            // write it on the board
  }, [])                                        // run once, on load

  return (
    <div>
      <h1>My Dashboard</h1>
      {scores.map(row => <p>{row.version}: {row.correct}</p>)}
    </div>
  )
}

export default App