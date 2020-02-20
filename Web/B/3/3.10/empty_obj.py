def func(a, b):
	print(a + b)

result = func(2, 17)
print(type(result))
print(result is None)

print(bool("" is None))

test_cases = (
	42,
	'',
	[1, 2],
	[],
	{},
	None,
	0
)

result = []
for entry in test_cases:
	if entry:
		result.append(1)
	if entry is None:
		result.append(0)
	print(result)


print("")
def my_func(sentiel=None, param=14):
	if sentiel is not None:
		print("Так не работает. Указывайте только именованные аргументы")
		return 
	return "пароли от всех секретов"

print(my_func(20))

print(my_func(param=20))
