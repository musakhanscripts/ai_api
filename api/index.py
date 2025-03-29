from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Initialize Hugging Face pipeline for text generation (AI model)
pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-V3-0324", trust_remote_code=True)

# Route to handle chat requests from Roblox
@app.route('/chat', methods=['POST'])
def chat():
    # Get the message from the player
    player_message = request.json.get('message')
    
    # Generate AI response using Hugging Face
    response = pipe([{"role": "user", "content": player_message}])

    # Return the response to Roblox
    return jsonify({"response": response[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
