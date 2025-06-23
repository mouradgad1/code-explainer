# ai_routes.py
import os
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ai = Blueprint("ai", __name__)

@ai.route("/api/explain", methods=["POST"])
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

@ai.route("/api/question", methods=["POST"])
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
