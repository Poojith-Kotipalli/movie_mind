from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def health():
    return "MovieMind API is running", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)