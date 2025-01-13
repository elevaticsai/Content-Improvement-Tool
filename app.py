from flask import Flask, render_template, request, jsonify
import requests
import logging
from requests.exceptions import RequestException
import socket

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def is_ollama_running():
    try:
        socket.create_connection(("localhost", 11434), timeout=1)
        return True
    except OSError:
        return False

@app.route('/')
def index():
    ollama_status = "Running" if is_ollama_running() else "Not Running"
    return render_template('index.html', ollama_status=ollama_status)

@app.route('/generate', methods=['POST'])
def generate():
    if not is_ollama_running():
        return jsonify({"error": "Ollama API is not running. Please start the Ollama service."}), 503

    data = request.json
    topic = data['topic']

    prompt = f"""
    Generate a brief content about the following topic:
    Topic: {topic}
    
    Please provide a concise and engaging paragraph of about 3-5 sentences.
    """

    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 40,
            "max_tokens": 200
        }
    }

    try:
        app.logger.info(f"Sending request to Ollama API: {OLLAMA_API_URL}")
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        generated_content = result['response'].strip()
        return jsonify({"generatedContent": generated_content})
    except RequestException as e:
        app.logger.error(f"Failed to connect to Ollama API: {str(e)}")
        return jsonify({"error": f"Failed to connect to Ollama API. Please check if the service is running and accessible."}), 500

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    content = data['content']
    tone = data['tone']
    style = data['style']
    length = data['length']

    prompt = f"""
    Improve the following email content:
    
    Original Content: {content}
    
    Desired Tone: {tone}
    Writing Style: {style}
    Desired Length: {length}
    
    Please provide an improved version of the email, analysis scores, and general feedback.
    """

    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 40,
            "max_tokens": 500
        }
    }

    response = requests.post(OLLAMA_API_URL, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        generated_content = result['response']
        
        # Here you would parse the generated_content to extract scores and feedback
        # For this example, we'll use placeholder values
        scores = {
            "spelling": 8.5,
            "grammar": 9.0,
            "vocabulary": 7.5,
            "clarity": 8.0,
            "readability": 8.5
        }
        
        overall_score = sum(scores.values()) / len(scores)
        
        return jsonify({
            "generatedContent": generated_content,
            "scores": scores,
            "overallScore": overall_score,
            "toneScore": tone.capitalize(),
            "lengthScore": f"Word Count: {len(content.split())}, Target: {length}"
        })
    else:
        return jsonify({"error": "Failed to generate content"}), 500

@app.route('/check_ollama', methods=['GET'])
def check_ollama():
    return jsonify({"status": "running" if is_ollama_running() else "not_running"})

if __name__ == '__main__':
    app.run(debug=True)