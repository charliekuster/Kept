// Exemplo em src/pages/Home.jsx
import React, { useEffect, useState } from 'react';
import api from '../services/api';
//import Sidebar from '../components/Sidebar/Sidebar';
import Table from '../components/tabela/table';
import Sidebar from '../components/Sidebar/Sidebar';

function Home() {
  const [dados, setDados] = useState([]);

  useEffect(() => {
    api.get('/klebsiela/bacteria/metadados') // Ex: FastAPI retorna dados em /meu-endpoint
      .then(response => {
        setDados(response.data);
      })
      .catch(error => {
        console.error('Erro ao buscar dados:', error);
      });
  }, []);

  return (
    <div>
        <Sidebar/>
        <Table/>
      {/*<pre>{JSON.stringify(dados, null, 2)}</pre> */} 
    </div>
  );
}

export default Home;

