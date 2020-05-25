import timeit


def Fibo(n):
    if n < 2:
        return n
    else:
        return Fibo(n - 1) + Fibo(n - 2)


cache = {0: 0, 1: 1}


def Fibo2(n):
    if n in cache:
        return cache[n]
    else:
        f = Fibo2(n - 1) + Fibo2(n - 2)
        cache[n] = f
        return f


# for n in [10, 20, 30]:
#     t_reg = timeit.Timer(lambda: Fibo(n)).repeat(number=1, repeat=1)[0]
#     t_mem = timeit.Timer(lambda: Fibo2(n)).repeat(number=1, repeat=1)[0]
#     print(f"Speed for n={n}:")
#     print(f" usual Fibo {t_reg:.5g} sec, memorized Fibo {t_mem:.5g} sec")
#     print(f"For n={n} memorized faster in {t_reg / t_mem:.3f} times!")

if __name__ == '__main__':
    Fibo2(2049)
