from Scraper import Scraper
import Config
import time

total = 0
num = 0

for i in range(50):
    start = time.time()
    s = Scraper()
    print str(i + 1) + " " + s.getBalance(Config.User, Config.Pass),
    delta = time.time() - start
    print delta,
    total += delta
    num += 1
    print "Average: " + str(total / num)
    s.cleanup()
