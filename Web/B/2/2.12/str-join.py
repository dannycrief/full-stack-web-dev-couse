words = ["Monty", "Python\'s", "flying", "circus"]
sentence = " ".join(words)
print(sentence)
s1 = "first string"
s2 = "second string"
s = s1 + s2
print(s)

print("")

s = " ".join([s1, s2])
print(s)

print("")

fruits = ["apple", "peach", "pineapple", "banana"]
sentence = "My favorite fruit salad consists of " + ", ".join(fruits)
print(sentence)

print("")

sentence = "Pretty long sentence with whitespaces as word delimiter."
words = sentence.split()
print(words)
resulting_string = "+".join(words)
print(resulting_string)
