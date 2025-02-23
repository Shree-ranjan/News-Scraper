import React from "react";
import NewsList from "./components/NewsList";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Super Bowl 2025 News</h1>
      </header>
      <main>
        <NewsList />
      </main>
    </div>
  );
}

export default App;