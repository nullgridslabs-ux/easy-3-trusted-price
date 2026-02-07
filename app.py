# easy-3-trusted-price/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/health")
def health():
    return "ok"

@app.route("/api/checkout", methods=["POST"])
def checkout():
    data = request.json or {}
    total = data.get("total")
    vip = data.get("vip")
    # BUG: trusts client state
    if vip and total == 1:
        return jsonify({"status":"ok","flag":FLAG})
    return jsonify({"status":"ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
