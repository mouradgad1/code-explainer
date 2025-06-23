import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/code_explainer.html")
def code_explainer():
    return render_template("code_explainer.html", project_name="Software Development")

@app.route("/api/explain", methods=["POST"])
def explain_code():
    code = request.json.get("code")
    try:
        messages = [
            {"role": "system", "content": "You are a helpful assistant tasked with explaining code."},
            {"role": "user", "content": code}
        ]
        response = client.chat.completions.create(
            model="gpt-4.1-nano-2025-04-14",
            messages=messages,
            max_tokens=300,  
            temperature=0.7
        )
        return jsonify({'explanation': response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/question", methods=["POST"])
def answer_question():
    question = request.json.get("question")
    try:
        messages = [
            {"role": "system", "content": (
                "You are a teacher helping programmers by answering their questions. "
                "The answer must be simple yet technical, divided into clear sections. "
                "Refuse to answer anything not related to programming."
            )},
            {"role": "user", "content": question}
        ]
        response = client.chat.completions.create(
            model="gpt-4.1-nano-2025-04-14",
            messages=messages,
            max_tokens=400,  
            temperature=0.7
        )
        return jsonify({'answer': response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
