from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <body>
            <h1>Sepsis Supervisor Agent</h1>
            <p>CI/CD validation application.</p>
            <p>Environment deployment successful.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy",
            "application": "sepsis-supervisor"
        }
    )


@app.route("/ask", methods=["POST"])
def ask():
    payload = request.get_json() or {}

    question = payload.get("question", "")

    return jsonify(
        {
            "question": question,
            "route": "DUMMY",
            "message": "Supervisor integration will be supplied by application team."
        }
    )