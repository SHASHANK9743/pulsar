from flask import Flask

from backend.app.api.main import api_router
from backend.app.core.config import Config

app = Flask(__name__)
app.config.update(Config().__dict__)
app.register_blueprint(api_router)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8532, )
