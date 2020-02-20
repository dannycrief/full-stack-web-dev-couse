import collections

# Task 1
print('Task 1')
searched_IP = '79.136.245.135'

fp = open('dummy-access.log', encoding='UTF-8')
read = fp.readlines()
fp.close()

count_ip = 0

for lines in read:
    lines = lines.split()
    if lines[0] == searched_IP:
        count_ip += 1

print(count_ip)

# Task 2
print('Task 2')
searched_IP = '127.0.0.1'
count_ip = 0
for lines in read:
    lines = lines.split()
    if lines[0] == searched_IP:
        count_ip += 1

print(count_ip)

# Task 3
print('Task 3')

new = []
for lines in read:
    new_list_of_ips = new.append(lines.split()[0])
c = collections.Counter(new)
c_m = c.most_common(1)[0]
print("The most popular IP. Times we see: {}".format(c_m[1]))

# Task 4
print('Task 4')

new = []
for lines in read:
    new_list_of_ips = new.append(lines.split()[0])
c = collections.Counter(new)
c_m = c.most_common(1)[0]
print("The most popular IP. What ip: {}".format(c_m[0]))

# Task 5
print('Task 5')
new = []
for lines in read:
    new_ips_list = new.append(lines.split()[0])
c = collections.Counter(new)
print(c.most_common()[-1])

# Task 6
print('Task 6')
new = []
all_req = 0
for lines in read:
    all_req += 1
    new_list = new.append(lines.split()[0])
c = collections.Counter(new)
ips_list = []
for ip in c:
    ips = ip.split()
    ips_list.append(ips)
    # print(ips)
total = 0

# number of clients
for elem_in_ips_list in ips_list:
    total += 1
# print(c)
# print(ips_list)
print("Nubers of requests: {}".format(all_req))
print("Numbers of clients: {}".format(total))
print("Numbers of requests from one client: {}".format(round(all_req/total), 0))

