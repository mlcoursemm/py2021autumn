import multiprocessing
import time
import logging

def print_proc(mes):
    name = multiprocessing.current_process().name
    print(f'Process {name}: {mes}')
    
def process_function(x):
    name = multiprocessing.current_process().name
    print_proc('starting')
    time.sleep(0.1)
    print_proc('finishing')
    return x**2

if __name__ == "__main__":
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    num_cores = multiprocessing.cpu_count()
    num_proc = 7#num_cores - 1 # not counting Main
    print_proc(f'number of cores = {num_cores}')
    xit = [i for i in range(1, num_proc + 1)]
    print_proc('before creating pool')
    pool = multiprocessing.Pool(processes=num_proc)
    print_proc('before running processes')
    res = pool.map(process_function, xit)
    print_proc(f'result of processes - {res}')
    print_proc('all done')