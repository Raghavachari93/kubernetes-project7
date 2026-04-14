from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    # simulate CPU work
    start = time.time()
    while time.time() - start < 0.2:
        pass
    return "Hello, Kubernetes Autoscaling 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
