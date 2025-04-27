import React, { useEffect, useState } from 'react';
import api from '../services/api';
import styles from  './bacteria.module.css'

function FilterItem({name}) {

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
      <div className={styles.container}>
        <button className={styles.iconButton}>
          <img src="" alt=" " />
        </button>      
        <button className={styles.textButton}>
          <p>{name}</p>
          <img src="" alt=" " />
        </button>
      </div>
    );
    
  }
  
  export default FilterItem;