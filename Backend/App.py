from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
import psycopg2
import cohere
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

App = Flask(__name__)
CORS(App)
bcrypt = Bcrypt(App)
App.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(App)

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
        access_token = create_access_token(identity=user_id)
        return jsonify({"message": "Signup successful", "token": access_token})
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
    
    access_token = create_access_token(identity=user[0])
    return jsonify({"message": "Login successful", "token": access_token})

@App.route('/generate_lyrics', methods=['POST'])
@jwt_required
def gen_lyrics():
    try:
        data = request.get_json()
        style = data.get('style')
        mood = data.get('mood')
        keywords = data.get('keywords')

        print(f"Recivied request - Stlye: {style}, Mood: {mood}, Keywords: {keywords}")

        prompt = f"Write a {style} song with a {mood} mood. Keywords are: {keywords}"

        response = co.generate(
            model='command',  # You can use 'xlarge' for high-quality text generation
            prompt=prompt,
            max_tokens=150  # Adjust the token count as needed
        )

        lyrics = response.generations[0].text.strip()
        return jsonify({"lyrics": lyrics})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    App.run(debug=True)