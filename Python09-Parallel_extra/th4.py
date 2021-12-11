import threading
import time

def thread_function():
    name = threading.current_thread().name
    print(f'Thread {name}: starting')
    time.sleep(2)
    print(f'Thread {name}: finishing')

if __name__ == "__main__":
    print('Main    : before creating thread')
    x = threading.Thread(target=thread_function, name='my_thread_1', daemon=True)
    print('Main    : before running thread')
    x.start()
    print('Main    : wait for the thread to finish')
    x.join()
    print('Main    : all done')