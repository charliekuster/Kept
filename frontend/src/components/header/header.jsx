import { Link } from 'react-router-dom';
import './header.css';


const Header = () => {
    return (
        <header>
            <div className="logo">
                <Link to="/">
                    <img src="/logos/site/kept.png" alt="Logo" />
                </Link>
            </div>
            <nav>
                <ul className="nav_links">
                    <li><Link to="/bacGenomes">GENOMES</Link></li>
                    <li><Link to="/upload">UPLOAD</Link></li>
                    <li><Link to="/documentation">DOCUMENTATION</Link></li>
                    <li><Link to="/about">ABOUT</Link></li>
                </ul>
            </nav>
            <div className="auth">
                <Link to="/login">Log in</Link>
                <span>|</span>
                <Link to="/signup">Sign up</Link>
            </div>
        </header>
    );
};

export default Header;
