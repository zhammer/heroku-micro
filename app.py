import os

import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
  return "Hello world!"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=os.getenv("PORT", "7070"))
