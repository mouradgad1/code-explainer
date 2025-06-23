# app.py
from flask import Flask, render_template
from ai_routes import ai

app = Flask(__name__)
app.register_blueprint(ai)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
