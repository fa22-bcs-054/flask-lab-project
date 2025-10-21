from flask import Flask, jsonify, request, render_template, send_from_directory, url_for
from datetime import datetime
import os

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    @app.route("/")
    def home():
        return render_template(
            "index.html",
            title="Flask Lab Project",
            year=datetime.now().year,
        )

    @app.route("/about")
    def about():
        return jsonify({
            "name": "Flask Lab Project",
            "version": "1.0.0",
            "description": "Minimal two-member lab app with tests, Dockerfile, and CI.",
        })

    @app.route("/health")
    def health():
        return "OK", 200

    @app.route("/data", methods=["POST"])
    def data():
        """
        Accept JSON or form data and echo it back in a friendly envelope.
        """
        # Safely parse JSON if present, otherwise use form data
        payload = request.get_json(silent=True)
        if payload is None:
            payload = request.form.to_dict()

        # Add a tiny metadata envelope
        response = {
            "received": payload,
            "meta": {
                "content_type": request.headers.get("Content-Type", ""),
                "client_ip": request.remote_addr,
                "timestamp": datetime.utcnow().isoformat() + "Z",
            },
        }
        return jsonify(response), 201

    # Optional: serve a favicon if you drop one in /static
    @app.route("/favicon.ico")
    def favicon():
        icon_path = os.path.join(app.static_folder, "favicon.ico")
        if os.path.exists(icon_path):
            return send_from_directory(app.static_folder, "favicon.ico")
        # fall back to a tiny 204 to avoid 404 noise
        return ("", 204)

    # Simple 404 page as JSON (nicer than plain HTML)
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not found", "path": request.path}), 404

    return app

# For `python app.py`
app = create_app()

if __name__ == "__main__":
    # Keep host/port the same; enable debug by setting FLASK_DEBUG=1 in your env if you like
    app.run(host="0.0.0.0", port=5000)
