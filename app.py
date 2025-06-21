import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", project_name="Software Development")

@app.route("/code-explainer")
def code_explainer():
    return render_template("code_explainer.html")

@app.route("/api/explain", methods=["POST"])
def explain_code():
    code = request.json.get("code")
    try:
        messages=[]
        messages.append({"role": "system", "content": "you are helpful assistant tasked with explaining code"})
        messages.append({"role": "user", "content": code})
        response = client.chat.completions.create(

            model="gpt-4.1-nano-2025-04-14",

            messages=messages,

            max_tokens=150,

            temperature=0.7

        )
        
        print (response.choices[0].message.content)
        return jsonify({'explanation': response.choices[0].message.content.strip()})

    except Exception as e:
        print (e)
        return jsonify({'error': str(e)}), 500
    # Static fake explanation
    

    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
