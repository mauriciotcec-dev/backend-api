from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)
BACKEND_DATA_URL = os.environ.get("BACKEND_DATA_URL", "http://backend-data:5001")

@app.route("/comments")
def comments():
    try:
        r = requests.get(f"{BACKEND_DATA_URL}/comments")
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
