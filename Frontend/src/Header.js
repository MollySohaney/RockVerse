// Header.js
import React from "react";
import { Link } from "react-router-dom";
import "./App.css";

function Header() {
    return (
        <header className="header">
            <h1>RockVerse</h1>
            <nav>
                <ul>
                    <li>
                        <Link to="/login">Login</Link>
                    </li>
                    <li>
                        <Link to="/signup">Signup</Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
