from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-V3-0324", trust_remote_code=True)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        player_message = request.json.get('message')
        if not player_message:
            return jsonify({"error": "No message provided"}), 400

        response = pipe([{"role": "user", "content": player_message}])

        return jsonify({"response": response[0]['generated_text']})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
