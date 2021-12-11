import threading
import concurrent.futures
import time

class AtomicUpdate:
    def __init__(self):
        self.val = 0
        self._lock = threading.Lock()

    def update(self, dx):
        name = threading.current_thread().name
        with self._lock:
            print(f'Thread {name}: starting to lock')
            val = self.val
            val += dx
            time.sleep(0.1)
            self.val = val
            print(f'Thread {name}: finishing lock')

if __name__ == "__main__":
    n_threads = 2
    obj = AtomicUpdate()
    print(f'Initial val = {obj.val}') 
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        executor.submit(obj.update, 1)
        executor.submit(obj.update, 2)
    print(f'Final val = {obj.val}')    
    print('Main    : done')