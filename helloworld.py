import os
from flask import Flask
from rest import rest

app = Flask(__name__)
app.register_blueprint(rest)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
