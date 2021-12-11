import threading
import concurrent.futures
import time

def thread_function(a):
    name = threading.current_thread().name
    print(f'Thread {name}-{a}: starting')
    time.sleep(2)
    print(f'Thread {name}-{a}: finishing')

if __name__ == "__main__":
    n_threads = 3
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        executor.map(thread_function, range(n_threads - 1))
        executor.submit(thread_function, n_threads - 1)
    print('Main    : done')