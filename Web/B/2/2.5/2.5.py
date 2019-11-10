FILENAME = 'input.txt'

reader = open(FILENAME)
lines = reader.readlines()
reader.close()

writer = open('output.txt', 'w')
lines_counter = 0

for line in lines:
    stripped_line = line.strip()
    if stripped_line:
        writer.write(stripped_line)
        writer.write('\n')
        lines_counter += 1

writer.close()
print(lines_counter)
