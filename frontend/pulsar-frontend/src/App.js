import './App.css';
import Header  from './Components/Header/Header';
import Body from './Components/Body/Body';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Header />
        <Body />
        <h1>This is my Doctor's buddy react Application.</h1>
      </header>
    </div>
  );
}
export default App;
