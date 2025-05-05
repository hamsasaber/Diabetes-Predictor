from flask import jsonify
from rules.rules_engine import evaluate_rules


def evaluate_rules_route(data):
    result = evaluate_rules(data)
    return jsonify(result)
