# easy-3-trusted-price/app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/")
def index():
    return """
<h2>Checkout API</h2>
<p>Handles promotional and VIP purchases.</p>
<ul>
<li>POST /api/checkout</li>
<li>GET /health</li>
</ul>
"""

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
