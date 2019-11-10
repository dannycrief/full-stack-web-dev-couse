names_len = {}
people = ["Bob", "Liza", "Anna", "Fanny", "Violet"]
for person in people:
    names_len[person] = len(person)

keys_ = list(names_len.keys())
keys_.sort()
print(keys_)

