from flask import Flask, render_template
from ai_routes import ai_blueprint
from ai_routes import ai_routes

app = Flask(__name__)
app.register_blueprint(ai_routes)
app.register_blueprint(ai_blueprint)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)