import collections
import random

c = collections.Counter()
print(c['key'])
print(c["k"])
c[32] += 1
print(c)

# the new one
print("")

c = collections.Counter()
for x in range(10):
    c[x] = random.randint(1, 100)
print(c.most_common(3))
print(c)
for key, value in c.most_common(3):
    print("{} - {}".format(key, value))

# the new one
print("")
a_string = "Calculate frequency of characters in this string"
c = collections.Counter(a_string)
print(c)
print(c.most_common())
