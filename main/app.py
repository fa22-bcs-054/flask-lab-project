from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Simple example of rendering a template
    return render_template("index.html", title="Flask Lab Project")

@app.route("/health")
def health():
    return "OK", 200

@app.route("/data", methods=["POST"])
def data():
    # Accepts JSON or form data
    if request.is_json:
        payload = request.get_json()
    else:
        payload = request.form.to_dict()
    return jsonify({"received": payload}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
