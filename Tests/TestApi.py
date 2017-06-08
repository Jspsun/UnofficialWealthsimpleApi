import Config
import time
import json
import requests

total = 0
num = 0

for i in range(50):
    start = time.time()

    p = {"email": Config.User, "password": Config.Pass, "attempts": 5}
    r = requests.get("http://localhost:1337/", json=p)
    data = json.loads(json.dumps(r.json()))
    if 'error' not in data:
        print str(i) + " " + str(data["Portfolio Value"]),

        delta = time.time() - start
        print delta,
        total += delta
        num += 1
        print "Average: " + str(total / num)
    else:
        print str(i) + " " + data["error"]
