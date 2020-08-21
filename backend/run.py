from flask import Flask
from api.runScript.main import run
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.register_blueprint(run)


if __name__ == '__main__':
    app.run(debug=True)
