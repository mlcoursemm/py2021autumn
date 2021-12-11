import multiprocessing
import concurrent.futures
import time
import logging

def print_proc(mes):
    name = multiprocessing.current_process().name
    print(f'Process {name}: {mes}')
    
def process_function(x, y):
    name = multiprocessing.current_process().name
    print_proc('starting')
    time.sleep(0.1)
    print_proc('finishing')
    return x + y

if __name__ == "__main__":
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    num_cores = multiprocessing.cpu_count()
    num_proc = 7#num_cores - 1 # not counting Main
    print_proc(f'number of cores = {num_cores}')
    print_proc('before creating & running pool')
    res_arr = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_proc) as executor:
        for i in range(1, num_proc+1):
            res_arr.append(executor.submit(process_function, i, i+1).result())
    print_proc(f'result of processes - {res_arr}')
    print_proc('all done')
 