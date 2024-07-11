import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => (
    <nav className="navbar">
        <div className="navbar-logo">
            <Link to="/">Top Products</Link>
        </div>
        <ul className="navbar-links">
            <li>
                <NavLink to="/" exact activeClassName="active">
                    Home
                </NavLink>
            </li>
            <li>
                <NavLink to="/categories/electronics/products" activeClassName="active">
                    Electronics
                </NavLink>
            </li>
            <li>
                <NavLink to="/categories/fashion/products" activeClassName="active">
                    Fashion
                </NavLink>
            </li>
        </ul>
    </nav>
);

export default Navbar;
