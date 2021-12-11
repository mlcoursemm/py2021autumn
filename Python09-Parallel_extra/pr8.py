import multiprocessing
import concurrent.futures
import time
import logging

def print_proc(mes):
    name = multiprocessing.current_process().name
    print(f'Process {name}: {mes}')
    
def process_function(x_d, x_s, x_a):
    time.sleep(0.1)
    name = multiprocessing.current_process().name
    print_proc('starting')
    with x_d.get_lock():
        x_d.value += 1
    with x_s.get_lock():
        x_s.value = x_s.value.upper()
    with x_a.get_lock():
        x_a[1] *= 2
    print_proc(f'x_d = {x_d.value}')
    print_proc(f'x_s = {x_s.value}')
    print_proc(f'x_a = {[a for a in x_a]}')   
    print_proc('finishing')

if __name__ == "__main__":
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    num_cores = multiprocessing.cpu_count()
    num_proc = num_cores - 1 # not counting Main
    print_proc(f'number of cores = {num_cores}')
    x_d = multiprocessing.Value('d', 0)
    x_s = multiprocessing.Array('c', b"Hello!")
    x_a = multiprocessing.Array('d', [1.0, 2.5, 4.0])
    print_proc(f'x_d = {x_d.value}')
    print_proc(f'x_s = {x_s.value}')
    print_proc(f'x_a = {[a for a in x_a]}')
    print_proc('before creating & running pool')
    
    processes = [multiprocessing.Process(target=process_function, args=(x_d, x_s, x_a)) for _ in range(num_proc)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()    

    print_proc('after finishing pool')
    print_proc(f'x_d = {x_d.value}')
    print_proc(f'x_s = {x_s.value}')
    print_proc(f'x_a = {[a for a in x_a]}')
    print_proc('all done')
 