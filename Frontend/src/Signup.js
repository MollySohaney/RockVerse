import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Header from "./Header";

function Signup() {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleSignup = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:5000/signup", {
                username,
                email,
                password,
            });

            navigate("/dashboard");
        } catch (error) {
            console.error("Signup error:", error.response.data);
        }
    };

    return (
        <div>
            <Header />
            <div class="signup-form">
                <h3>Sign Up</h3>
                <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
                <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
                <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
                <button onClick={handleSignup}>Sign Up</button>
            </div>
        </div>
    );
}

export default Signup;
