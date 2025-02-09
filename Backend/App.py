from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

App = Flask(__name__)
CORS(App)

openai.api_key = os.getenv("OPENAI_API_KEY")


@App.route('/generate_lyrics', methods=['POST'])
def gen_lyrics():
    try:
        data = request.get_json()
        style = data.get('style')
        mood = data.get('mood')
        keywords = data.get('keywords')

        print(f"Recivied request - Stlye: {style}, Mood: {mood}, Keywords: {keywords}")

        prompt = f"Write a {style} song with a {mood} mood. Keywords are: {keywords}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        lyrics = response.generations[0].text
        return jsonify({"lyrics": lyrics})
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    App.run()