from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_session import Session
import psycopg2
import cohere
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

App = Flask(__name__)
CORS(App)
App.config["SECRET_KEY"] = os.getenv("SESSION_SECRET_KEY") 
Session(App)
bcrypt = Bcrypt(App)

DB_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DB_URL)
cursor = conn.cursor()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

@App.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400
    
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    try:
        cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s) RETURNING id",
                       (username, email, password_hash))
        user_id = cursor.fetchone()[0]
        conn.commit()
        session['user_id'] = user_id
        return jsonify({"message": "Signup successful"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@App.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    cursor.execute("SELECT id, password_hash FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if not user or not bcrypt.check_password_hash(user[1], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    session['user_id'] = user[0]
    return jsonify({"message": "Login successful"})

@App.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully"})

@App.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"message": "Welcome to your dashboard!"})

@App.route('/generate_lyrics', methods=['POST'])
def gen_lyrics():
    try:
        data = request.get_json()
        style = data.get('style')
        mood = data.get('mood')
        keywords = data.get('keywords')

        print(f"Recivied request - Stlye: {style}, Mood: {mood}, Keywords: {keywords}")

        prompt = f"Write a {style} song with a {mood} mood. Keywords are: {keywords}"

        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=150
        )

        lyrics = response.generations[0].text
        return jsonify({"lyrics": lyrics})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    App.run(debug=True)