import os
import sys
import logging
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
from openai import OpenAI

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Log environment variables (except sensitive ones)
logger.info("Starting application...")
logger.info(f"Python version: {sys.version}")
logger.info(f"OpenAI version: {openai.__version__}")
logger.info(f"Environment variables: { {k: v for k, v in os.environ.items() if 'KEY' not in k and 'SECRET' not in k} }")

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
try:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        logger.error("OPENAI_API_KEY environment variable is not set")
        sys.exit(1)
    client = OpenAI(api_key=openai_api_key)
    logger.info("Successfully initialized OpenAI client")
except Exception as e:
    logger.error(f"Failed to initialize OpenAI client: {str(e)}")
    sys.exit(1)

@app.route("/")
def index():
    try:
        logger.info("Rendering index.html")
        # Verify template exists
        template_path = os.path.join('templates', 'index.html')
        if not os.path.exists(template_path):
            logger.error(f"Template not found at: {os.path.abspath(template_path)}")
            return f"Template not found: {template_path}", 500
            
        return render_template("index.html", project_name="Software Development")
    except Exception as e:
        logger.error(f"Error rendering index.html: {str(e)}", exc_info=True)
        return f"An error occurred while loading the page: {str(e)}", 500

@app.route("/code-explainer")
def code_explainer():
    try:
        return render_template("code_explainer.html")
    except Exception as e:
        logger.error(f"Error rendering code_explainer.html: {str(e)}")
        return "An error occurred while loading the code explainer. Please check the logs for more details.", 500

@app.route("/api/explain", methods=["POST"])
def explain_code():
    code = request.json.get("code")
    try:
        messages=[]
        messages.append({"role": "system", "content": "you are helpful assistant tasked with explaining code"})
        messages.append({"role": "user", "content": code})
        response = client.chat.completions.create(

            model="gpt-4.1-nano-2025-04-14",  # Using a valid model name

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
