from flask import Flask
from medication.routes import medication_bp

import sys

app = Flask(__name__)


app.register_blueprint(medication_bp, url_prefix='/medication')


if __name__ == '__main__':
    #DO not remove any Code below
    port = int(sys.argv[1])
    app.run(debug=True, host="0.0.0.0", port=port)
