import time


def benchmark(iterations):
    def decorator(func):
        def wrapper(*arg, **kwarg):
            total_time = 0
            # список для хранения total_time
            total_time_list = []

            for i in range(iterations):
                start_time = time.time()
                value = func(*arg, **kwarg)
                end_time = time.time()
                total_time += end_time - start_time
                total_time_list.append(total_time)
            # max min время выполнения функции
            min_time = min(total_time_list)
            max_time = max(total_time_list)
            # среднее время выполнения функции
            AvvgTime = total_time / iterations
            print('--- BENCMARK_RESULT ---')
            print()
            print(
                'Function_name                  | AvvgTime, sec    | Iterations  | Time full iterations, sec  | Time 1 iterations, sec |')
            print(
                '-----------------------------------------------------------------------------------------------------------------------')
            print('{: ^30} | {: ^16.10f} | {: ^12.2f}|  {: ^22.10f} | {: ^25.10f} |'.format(func.__name__, AvvgTime,
                                                                                            iterations, max_time,
                                                                                            min_time))

            return value

        return wrapper

    return decorator


# задайте количество итераций
@benchmark(iterations=10)
# напишите здесь свою функцию
def cycle():
    for j in range(1000000):
        pass


# вызов вашей функции
cycle()