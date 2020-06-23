# lambda arguments: function
a = lambda x: x

a = (lambda x: x * x)(3)
print(a)  # 9
a = (lambda x, y: x + y)(2, 3)
print(a)  # 5

ll = ['a', 'aa', 'b', 'bbb', 'c']
print(sorted(ll, key=lambda x: x.upper()))  # ['a', 'aa', 'b', 'bbb', 'c']
l = [1, 2, 3]
print(list(map(lambda x: x * x, l)))  # [1, 4, 9]
ll = [-1, -2, 3, 4, -22]
print(list(filter(lambda x: x > 0, ll)))  # [3, 4]

