import React from 'react';
import '../../../css/App.css';
import logo from '../../../images/logo.jpg';

function App() {
  return (
    <div className="root">
      <div className="App">
        <header className="App-header">
          
          <img className="App-logo" src={logo} alt="logo"/>
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    </div>
  );
}

export default App;
