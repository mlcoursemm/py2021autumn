import threading
import concurrent.futures
import time

def show(loc):
    name = threading.current_thread().name
    try:
        val = loc.val
    except AttributeError:
        print(f'Thread {name}, value=???')
    else:
        print(f'Thread {name}, value={val}')

def thread_init(loc, v):
    time.sleep(0.1)
    show(loc)
    loc.val = v
    show(loc)
   

if __name__ == '__main__':
    loc = threading.local()
    thread_init(loc, 0)
    n_threads = 2
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        executor.submit(thread_init, loc, 1)
        executor.submit(thread_init, loc, 2)
    show(loc)     
