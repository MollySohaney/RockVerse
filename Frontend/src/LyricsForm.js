import React, { useState } from "react";
import axios from "axios";

const LyricsForm = ({ setLyrics }) => {
  const [style, setStyle] = useState("Classic Rock");
  const [mood, setMood] = useState("Energetic");
  const [keywords, setKeywords] = useState("");

  const generateLyrics = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/dashboard", {
        style,
        mood,
        keywords,
      });
      setLyrics(response.data.lyrics);
      console.log("API Response:", response.data);
    } catch (error) {
      console.error("Error generating lyrics:", error);
    }
  };

  return (
    <div class="lyrics-form">
      <label>Style:</label>
      <select value={style} onChange={(e) => setStyle(e.target.value)}>
        <option>Classic Rock</option>
        <option>Metal</option>
        <option>Punk</option>
        <option>Grunge</option>
      </select>

      <label>Mood:</label>
      <select value={mood} onChange={(e) => setMood(e.target.value)}>
        <option>Energetic</option>
        <option>Dark</option>
        <option>Emotional</option>
      </select>

      <label>Keywords:</label>
      <input type="text" value={keywords} onChange={(e) => setKeywords(e.target.value)} placeholder="e.g. love, rebellion, thunder" />

      <button onClick={generateLyrics}>Generate Lyrics</button>
    </div>
  );
};

export default LyricsForm;
