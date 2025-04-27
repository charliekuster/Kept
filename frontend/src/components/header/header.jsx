import React from 'react';
import './header.css';

const Header = () => {
    return (
        <header>
            <div className="logo">
                <a href="/index.html">
                    <img src="/Imagens/Logos/Site/logo.png" alt="Logo" />
                </a>
            </div>
            <nav>
                <ul className="nav_links">
                    <li><a href="/genomes/indexGenomes.html">GENOMES</a></li>
                    <li><a href="/upload/indexUpload.html">UPLOAD</a></li>
                    <li><a href="/documentation/indexDoc.html">DOCUMENTATION</a></li>
                    <li><a href="indexAbout.html">ABOUT</a></li>
                </ul>
            </nav>
            <div className="auth">
                <a href="">Log in</a>
                <span>|</span>
                <a href="">Sign up</a>
            </div>
        </header>
    );
};

export default Header;
