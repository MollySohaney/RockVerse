import React, { useState } from "react";
import LyricsForm from "./LyricsForm";
import LyricsDisplay from "./LyricsDisplay.js";
import "./App.css";
import Header from "./Logged_Header";

function Dashboard() {
    const [lyrics, setLyrics] = useState("");
    return (
        <div>
            <Header />
            <div>
                <h4> Dashboard </h4>
                <LyricsForm setLyrics={setLyrics} />
                <LyricsDisplay lyrics={lyrics} />
            </div>
        </div>
    );
}

export default Dashboard