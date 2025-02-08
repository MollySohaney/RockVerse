import React, { use, useState } from "react";
import axios from "axios";

const LyricsForm = ({ setLyrics }) => {
    const [style, setStyle] = useState("Classical Rock");
    const [mood, setMood] = useState("Energetic");
    const [keywords, setKeywords] = useState("");
    const generateLyrics = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:5000/generate_lyrics", {
                style,
                mood,
                keywords,
            });
            setLyrics(response.data.lyrics);
            console.log("API Respinse", response.data)
        } catch (error) {
            console.error("Error generating lyrics", error);
        }
    };

    return (

        <div>
            <label>HelloWorld</label>
        </div>
    )
};

export default LyricsForm;