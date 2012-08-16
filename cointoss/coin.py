import random


r = random.Random(seed)
for check in xrange(1000000):
    print r.choice(["Alice", "Bob"])
print seed
