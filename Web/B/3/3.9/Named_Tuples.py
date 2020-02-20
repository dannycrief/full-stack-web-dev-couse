from collections import namedtuple

User = namedtuple("User", ["name", "age", "email"])

peter = User(name="Peter", age=32, email="peterrobinson@mail.com")
print(peter.name)

from math import sqrt

Point = namedtuple("Point", ["x", "y"])
p1 = Point(1, 2)
p2 = Point(1, 5)


distance = sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
print(distance)
