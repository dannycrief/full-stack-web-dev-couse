import time

t0 = time.time()
for j in range(1000000):
    pass

t1 = time.time()
print("Выполнение заняло %.5f секунд" % (t1 - t0))
