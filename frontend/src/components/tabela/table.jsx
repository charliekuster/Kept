import React, { useEffect, useState } from "react";
import api from '../../services/api';
import "./table.css";

const Table = ({dados}) => {

  return (
    <div className="table-container">
      <table>
        <thead>
          <tr>
            <th>ID LEMC</th>
            <th>ID</th>
            <th>Fasta</th>
            <th>Type of sample</th>
            <th>Host</th>
            <th>Isolation source</th>
            <th>Collection date</th>
            <th>Geographic location</th>
            <th>City</th>
            <th>State</th>
            <th>Country</th>
            <th>Biobank</th>
            <th>Biobank location</th>
            <th>Sequencing platform_1</th>
            <th>Assembly method</th>
            <th>Annotation method</th>
            <th>Organism</th>
            <th>Kapsule Locus</th>
            <th>Carbapenem resistance</th>
            
            
          </tr>
        </thead>
        <tbody>
          {dados.length > 0 ? (
            dados.map((item, index) => (
              <tr key={index}>
                <td>{item["ID LEMC"]}</td>
                <td>{item["ID"]}</td>
                <td>{item["Fasta"]}</td>
                <td>{item["Type of sample"]}</td>
                <td>{item["Host"]}</td>
                <td>{item["Isolation source"]}</td>
                <td>{item["Collection date"]}</td>
                <td>{item["Geographic location"]}</td>
                <td>{item["City"]}</td>
                <td>{item["State"]}</td>
                <td>{item["Country"]}</td>
                <td>{item["Biobank"]}</td>
                <td>{item["Biobank location"]}</td>
                <td>{item["Sequencing platform_1"]}</td>
                <td>{item["Assembly method"]}</td>
                <td>{item["Annotation method"]}</td>
                <td>{item["Organism"]}</td>
                <td>{item["Kapsule Locus"]}</td>
                <td>{item["Carbapenem resistance"]}</td>
                
                
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="19">No data available</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
