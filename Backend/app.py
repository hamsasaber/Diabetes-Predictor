from flask import Flask, request, jsonify
from routes.rules import evaluate_rules_route

app = Flask(__name__)


@app.route("/")
def index():
    return "Diabetes Prediction Flask API is running"


@app.route("/rules", methods=["POST"])
def rules_route():
    data = request.get_json()
    return evaluate_rules_route(data)


if __name__ == "__main__":
    app.run(debug=True)
