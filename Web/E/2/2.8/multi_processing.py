import multiprocessing as mp
import random
import time


def worker(i):
    interval = random.randint(0, 5)
    time.sleep(interval)
    print('Worker # % s is sleeping for % s seconds' % (str(i), str(interval)))


def main():
    pool = mp.Pool(2)
    results = pool.map(worker, range(5))
    return results


if __name__ == '__main__':
    results = main()
