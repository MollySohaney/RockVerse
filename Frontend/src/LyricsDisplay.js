import React from "react";

const LyricsDisplay = ({ lyrics }) => {
    return (
        <div>
            <h2>Generated Lyrics</h2>
            <pre>{lyrics}</pre>
        </div>
    );
};
export default LyricsDisplay;