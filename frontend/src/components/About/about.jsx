import React from 'react';
import './about.css';

const KlebsiellaIntro = () => {
  return (
    <>
      <div className="back_rosa">
        <h1>Klebsiella Database</h1>
      </div>

      <div className="kleb_data">
        <p>
          The <strong>Klebsiella-Phage SuscepTibility Database (KEPT)</strong> project aims to develop a database
          that integrates sequencing data with bacterial-phage susceptibility profiles to support the creation of an
          AI-driven tool for predicting phage efficacy. The project focuses on Klebsiella pneumoniae and its phages.
          A key component involves the automation of bioinformatic analyses for new bacterial and phage sequences,
          with the goal of offering an online, freely accessible version on our website. In the consolidation phase,
          we plan to make the database publicly available.
        </p>
        <p>
          As a project mainly funded by the <strong>Antimicrobial Resistance Institute of São Paulo (ARIES)</strong>,
          a FAPESP (Fundação de Amparo à Pesquisa do Estado de São Paulo)-supported research center, the database
          primarily integrates bacterial strains and bacteriophages from Brazil.
        </p>
        <p>
          We encourage interested researchers who wish to contribute and help expand the project to contact the main investigator.
        </p>
      </div>

      <div className= "teamText">
        <h2>Team</h2>
        <p>
          The multidisciplinary team recounts physicians, microbiologists, bioinformaticians and computational scientists
          from different universities and institutions. The main investigators of this project are:
        </p>
      </div>
    </>
  );
};

export default KlebsiellaIntro;
