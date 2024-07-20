from flask import Flask

from backend.app.api.main import api_router

app = Flask(__name__)
app.register_blueprint(api_router)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8532, debug=False)
