from flask import Flask
from view import add_url_rules

app = Flask(__name__)

add_url_rules(app)

app.run(host="0.0.0.0", port=5000)

