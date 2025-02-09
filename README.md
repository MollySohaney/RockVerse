# RockVerse

Name: Molly Sohaney

Welcome to RockVerse, a web application where users can generate rock lyrics based on their desired style, mood, and keywords. This project uses session-based authentication and AI-powered lyrics generation with the Cohere API.

Features
- User Authentication: Users can sign up, log in, and access a personalized dashboard.
- Lyric Generation: Generate rock lyrics by specifying style, mood, and keywords.
- Session-Based Authentication: Ensures that only logged-in users can access the dashboard.
- Responsive Design: The app is fully responsive and user-friendly across devices.

Technologies Used
Frontend:
- React.js
- React Router
- Axios for API calls
- CSS for styling

Backend:
- Flask (Python)
- Session-based Authentication with Flask-Session
- Cohere API for text generation

Database:
- PostgreSQL (for user authentication)

Challenges:
- Session Management: Implementing session-based authentication in Flask was initially challenging because of session cookie handling. After reading the Flask documentation and experimenting with Flask-Session, I successfully managed session data on the server-side and stored user information in cookies.
- Cohere API Integration: Integrating the Cohere API required understanding its prompt-based system and managing API requests. I used the cohere Python package to send prompts and retrieve lyrics.
- Frontend-Backend Communication: Handling user inputs in the frontend and ensuring secure API requests from React to Flask was a learning curve. I used Axios for making API requests from React and managed state using useState hooks.