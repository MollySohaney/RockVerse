import React, { useState } from "react";
import LyricsForm from "./LyricsForm";
import LyricsDisplay from "./LyricsDisplay.js";
import "./App.css";

function App() {
    const [lyrics, setLyrics] = useState("");
    return (
        <div>
            <h1> RockVerse </h1>
            <LyricsForm setLyrics={setLyrics} />
            <LyricsDisplay lyrics={lyrics} />
        </div>
    );
}

export default App