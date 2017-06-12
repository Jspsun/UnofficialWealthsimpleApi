from flask import Flask, json, request
import os
from Scraper import Scraper

app = Flask(__name__)


# Post a json to flask server


@app.route('/', methods=['Post', 'Get'])
def api_root():
    # validate that user sends in a json
    if request.headers['Content-Type'] != 'application/json':
        return "Please post a JSON"

    # data is a map of all the json input
    data = json.loads(json.dumps(request.json))

    # validate JSON
    if not('email' in data and 'password' in data and 'attempts' in data):
        return "Please post valid JSON"

    S = Scraper()
    portfolioValue = S.getBalance(
        data['email'], data['password'], data['attempts'])
    S.cleanup()

    if not portfolioValue:
        return json.dumps({"error": "error. Servers Unresponsive. Check your log in info"}), 500
    # making something to return
    returnJSON = {'Portfolio Value': portfolioValue}
    return json.dumps(returnJSON), 200


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 1337))
    app.run(debug=False, host='0.0.0.0', port=port)
