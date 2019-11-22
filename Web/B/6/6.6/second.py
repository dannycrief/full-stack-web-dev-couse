path = input("Enter the path to your file: ")

print("I'll try to count every line in your file", path)
try:
    f = open(path)
except FileNotFoundError:
    print("I can't find your file. Check the path..")
else:
    lines = f.readlines()
    lines_number =len(lines)
    print("Number of line: ", lines_number)
    f.close()