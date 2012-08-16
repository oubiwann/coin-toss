import random
from datetime import datetime


#seed = datetime.now().isoformat()
seed = "2012-08-16T09:56:45.098810"
r = random.Random(seed)
for check in xrange(1000000):
    print r.choice(["Alice", "Bob"])
print seed
