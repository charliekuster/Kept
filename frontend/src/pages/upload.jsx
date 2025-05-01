import React, { useEffect, useState } from 'react';
import api from '../services/api';
import Table from '../components/tabela/table';
import Sidebar from '../components/Sidebar/Sidebar';
import Header from '../components/header/header';
import LogoSection from '../components/LogoSection/LogoSection';
import Footer from '../components/Footer/Footer';

function BacGenoma() {
  const [dados, setDados] = useState([]);
  const [filteredData, setFilteredData] = useState([]);

  useEffect(() => {
    api.get('/klebsiela/bacteria/metadados')
      .then(response => {
        setDados(response.data);
        setFilteredData(response.data); // Define os dados iniciais
      })
      .catch(error => {
        console.error('Erro ao buscar dados:', error);
      });
  }, []);

  // Aplica os filtros selecionados
  const applyFilters = (selectedFilters) => {
    let filtered = [...dados];

    // Aplica filtro para cada campo
    for (const [campo, values] of Object.entries(selectedFilters)) {
      if (values.length > 0) {
        filtered = filtered.filter((item) => values.includes(item[campo]));
      }
    }

    setFilteredData(filtered);
  };

  // Limpa todos os filtros e exibe os dados originais
  const clearFilters = () => {
    setFilteredData(dados);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <Header />
        <LogoSection/>
        <Footer />
    </div>
  );
}

export default BacGenoma;
