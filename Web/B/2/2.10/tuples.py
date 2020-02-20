myTuple = tuple()
myTuple = tuple("String")
print(myTuple)

newTuple = tuple()
newTuple = ('element')
newTuple = (1, 'string', [2, 3])
newTuple = 42, 'sting elemen of tuple', ['44', 21]
print(newTuple)

print("")

t1 = (5, 'Alice')
t2 = (3, 'Bob')

d = {t1: 27, t2: 42}
print(d)
print(d[t1])

print('')

a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for items in a_tuple:
    print(items)
len(a_tuple)
a_tuple = tuple("Pretty long string")
print(a_tuple[0])

for index in range(len(a_tuple)):
    print(a_tuple[index])


