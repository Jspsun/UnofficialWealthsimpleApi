import Config
import time
import json
import requests

total = 0
num = 0

for i in range(50):
    start = time.time()

    p = {"email": Config.User, "password": Config.Pass}
    r = requests.get("http://localhost:1337/", json=p)
    data = r.json()
    print data,

    delta = time.time() - start
    print delta,
    total += delta
    num += 1
    print "Average: " + str(total / num)
