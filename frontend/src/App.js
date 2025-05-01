import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home';
import Genomes from './pages/bacGenoma';
import Upload from './pages/upload';
import Documentation from './pages/documentation';
import About from './pages/about';
import './App.css';


function App() {
  return (
    <Router>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/bacGenomes" element={<Genomes />} />
      <Route path="/upload" element={<Upload />} />
      <Route path="/documentation" element={<Documentation />} />
      <Route path="/about" element={<About />} />
    </Routes>
  </Router>

  );
}

export default App;
