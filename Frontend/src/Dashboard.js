import React, { useState } from "react";
import LyricsForm from "./LyricsForm";
import LyricsDisplay from "./LyricsDisplay.js";
import "./App.css";

function Dashboard() {
    const [lyrics, setLyrics] = useState("");
    return (
        <div>
            <h4> Dashboard </h4>
            <LyricsForm setLyrics={setLyrics} />
            <LyricsDisplay lyrics={lyrics} />
        </div>
    );
}

export default Dashboard