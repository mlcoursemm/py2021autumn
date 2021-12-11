import threading
import concurrent.futures
import time

class NonAtomicUpdate:
    def __init__(self):
        self.val = 0

    def update(self, dx):
        name = threading.current_thread().name
        print(f'Thread {name}: starting')
        val = self.val
        val += dx
        time.sleep(0.1)
        self.val = val
        print(f'Thread {name}: finishing')

if __name__ == "__main__":
    n_threads = 2
    obj = NonAtomicUpdate()
    print(f'Initial val = {obj.val}') 
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_threads) as executor:
        executor.submit(obj.update, 1)
        executor.submit(obj.update, 2)
    print(f'Final val = {obj.val}')    
    print('Main    : done')