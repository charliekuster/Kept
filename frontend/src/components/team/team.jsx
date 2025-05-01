import React from 'react';
import './team.css';

const members = [
  {
    name: 'Dr. med Iris Najjar, MD',
    img: '/Imagens/Iris.png',
    desc: `Laboratório Alerta, Division of Infectious Diseases, Escola Paulista de Medicina, Universidade Federal de São Paulo, São Paulo, Brazil;
    Department of Infectious Diseases, Hôpitaux Universitaires de Genève, Geneva, Switzerland.`,
    linkedin: 'https://www.linkedin.com/in/iris-najjar-a9b372120/',
    email: 'iris.najjar@gmail.com',
  },
  {
    name: 'Prof. Ana C. Gales',
    img: '/Imagens/image.png',
    desc: `Laboratório Alerta, Division of Infectious Diseases, Escola Paulista de Medicina, Universidade Federal de São Paulo, São Paulo, Brazil;
    Antimicrobial Resistance Institute of São Paulo, Universidade Federal de São Paulo, São Paulo, Brazil.`,
    linkedin: 'https://linkedin.com',
    email: 'email@example.com',
  },
  {
    name: 'Prof. Daniela Leal Musa',
    img: '/Imagens/Musa.png',
    desc: `Instituto de Ciência e Tecnologia, Universidade Federal de São Paulo, São Jose dos Campos, Brazil.`,
    linkedin: 'https://www.linkedin.com/in/daniela-musa-83850213/',
    email: 'musa@unifesp.br',
  },
  {
    name: 'Prof. Marcos G. Quiles',
    img: '/Imagens/quiles.png',
    desc: `Instituto de Ciência e Tecnologia, Universidade Federal de São Paulo, São Jose dos Campos, Brazil.`,
    linkedin: 'https://www.linkedin.com/in/marcos-g-quiles/',
    email: 'quiles@unifesp.br',
  },
  {
    name: 'Prof. Reginaldo Massanobu Kuroshu',
    img: '/Imagens/reginaldo.png',
    desc: `Instituto de Ciência e Tecnologia, Universidade Federal de São Paulo, São Jose dos Campos, Brazil.`,
    linkedin: 'https://linkedin.com',
    email: 'rmkuroshu@unifesp.br',
  },
  {
    name: 'Prof. Fernanda F. Santos',
    img: '/Imagens/FotoFernanda.jpg',
    desc: `Department of Microbiology, Immunology and Parasitology, Escola Paulista de Medicina, Universidade Federal de São Paulo, São Paulo, Brazil.`,
    linkedin: 'https://linkedin.com',
    email: 'email@example.com',
  },
  {
    name: 'Louise Texeira, PhD',
    img: '/Imagens/image.png',
    desc: `London School of Hygiene and Tropical Medicine, Department of Infection Biology, London, United Kingdom.`,
    linkedin: 'https://linkedin.com',
    email: 'email@example.com',
  },
  {
    name: 'Matheus Naves, Master student',
    img: '/Imagens/matheus.png',
    desc: `Laboratório Especial de Micologia, Escola Paulista de Medicina, UNIFESP, Brazil.`,
    linkedin: 'https://linkedin.com',
    email: 'email@example.com',
  },
];

const Team = () => {
  return (
    <div className="team">
      {members.map((member, index) => (
        <div className="card" key={index}>
          <div className="profile-image">
            <img src={member.img} alt={`Foto de ${member.name}`} />
          </div>
          <div className="conteudo">
            <div className="info">
              <h2>{member.name}</h2>
              <p>{member.desc}</p>
            </div>
            <div className="contact-icons">
              <a href={member.linkedin} target="_blank" rel="noopener noreferrer" className="icon linkedin">
                <img src="/Icons/about/Group.png" alt="LinkedIn" />
              </a>
              <a href={`mailto:${member.email}`} className="icon email">
                <img src="/Icons/about/Mail.png" alt="Email" />
              </a>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Team;
