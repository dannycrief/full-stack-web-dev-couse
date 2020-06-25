import threading
import timeit

import requests


def request_send():
    res = requests.request(method='get', url='http://google.com')
    return res


def main():
    threads = []
    start = timeit.default_timer()
    for i in range(100):
        t = threading.Thread(target=request_send)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = timeit.default_timer() - start
    return end


if __name__ == '__main__':
    main()
