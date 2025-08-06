from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend access from any domain

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    command = data.get('command', '').lower()

    # Basic logic
    if "hello" in command:
        response = "Hello sir, how can I help you?"
    elif "weather" in command:
        response = "The weather is great today!"
    else:
        response = "I'm sorry, I didn't understand that."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run()
