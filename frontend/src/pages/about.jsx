import React, { useEffect, useState } from 'react';
import api from '../services/api';
import Table from '../components/tabela/table';
import Sidebar from '../components/Sidebar/Sidebar';
import Header from '../components/header/header';
import LogoSection from '../components/LogoSection/LogoSection';
import Footer from '../components/Footer/Footer';
import TeamSection from '../components/About/about';
import Team from '../components/team/team';



function BacGenoma() {

  return (
    <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>


    
        <Header />
        <TeamSection/>
        <Team/>
        <LogoSection/>
        <Footer />

    </div>
  );
}

export default BacGenoma;

