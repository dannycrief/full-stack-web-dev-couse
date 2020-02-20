import time


def time_this(num_runs):
    def decorator_wrapper(run_func):
        def func(*args, **kwargs):
            num = 0
            for _ in range(num_runs):
                t0 = time.time()
                run_func(*args, **kwargs)
                t1 = time.time()
                num += (t1 - t0)
            num /= num_runs
            function = run_func.__name__
            print("Average run time in %s starts: %.5f seconds" % (num_runs, num))

        return func

    return decorator_wrapper


@time_this(num_runs=10)
def mainFunctinoToRun():
    for j in range(1000000):
        pass


mainFunctinoToRun()
