import multiprocessing
import concurrent.futures
import time
import logging

data = [1, 2, 3]

def print_proc(mes):
    name = multiprocessing.current_process().name
    print(f'Process {name}: {mes}')
    
def process_function(x):
    name = multiprocessing.current_process().name
    print_proc('starting')
    data.append(x)
    print_proc(f'data = {data}')
    time.sleep(0.1)
    print_proc('finishing')

if __name__ == "__main__":
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    num_cores = multiprocessing.cpu_count()
    num_proc = num_cores - 1 # not counting Main
    print_proc(f'number of cores = {num_cores}')
    print_proc(f'data = {data}')
    print_proc('before creating & running pool')
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_proc) as executor:
        executor.map(process_function, range(100, num_proc+100))
    print_proc(f'data = {data}')
    print_proc('all done')
 