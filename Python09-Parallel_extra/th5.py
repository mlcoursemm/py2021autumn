import threading
import time

def thread_function():
    name = threading.current_thread().name
    print(f'Thread {name}: starting')
    time.sleep(2)
    print(f'Thread {name}: finishing')

if __name__ == "__main__":
    threads = list()
    n_threads = 3
    for i in range(n_threads):
        th_name = f'my_thread_{i}'
        print(f'Main    : before creating and starting {th_name}')
        x = threading.Thread(target=thread_function, name=th_name)
        threads.append(x)
        x.start()
        
    for i in range(n_threads): 
        th_name = f'my_thread_{i}'
        print(f'Main    : before join {th_name}')
        threads[i].join()
        print(f'Main    : {th_name} done')
    
    print('Main    : done')