
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def root():
    result_of_get = requests.get(
        "http://staging.bldt.ca/api/method/build_it.test.get_students")
    result_json = result_of_get.json()
    result = []
    if result_json.get("status", False):
        print(result_json.get("message", "fetch data!"))
        result = result_json.get("data", [])
    return render_template("index.html", students=result)


if __name__ == '__main__':
    app.run(debug=True)
