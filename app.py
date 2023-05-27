from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

API_KEY = open('api_key.txt').read()
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# gpt-4
# gpt-3.5-turbo
def generate_chat_completion(messages, model="gpt-3.5-turbo", temperature=1, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

@app.route('/api/generate', methods=['POST'])
def generate_response():
    messages = request.get_json()
    try:
        response_text = generate_chat_completion(messages)
        return jsonify({'response': response_text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
