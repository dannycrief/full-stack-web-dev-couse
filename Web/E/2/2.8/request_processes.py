import multiprocessing as mp
import timeit

import requests


def send_request():
    res = requests.request(method='get', url='http://google.com')
    return res


def main():
    pool = mp.Pool(2)
    start = timeit.default_timer()

    results = []
    pool.map(send_request, range(10000))
    end = timeit.default_timer() - start
    return end


if __name__ == '__main__':
    main()
