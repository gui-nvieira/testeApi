from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello():
    x = {
  "name": "John",
  "age": 30,
  "city": "New York"
    }

    return json.dumps(x)



if __name__ == "__main__":
    app.run(host='0.0.0.0')