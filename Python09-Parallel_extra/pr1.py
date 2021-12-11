import multiprocessing
import time
import logging

def process_function(v):
    name = multiprocessing.current_process().name
    print(f'Process {name} (arg={v}): starting')
    time.sleep(2)
    print(f'Process {name} (arg={v}): finishing')

if __name__ == "__main__":
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    print('Main    : before creating process')
    x = multiprocessing.Process(target=process_function, args=(111,), name='my_process_1')
    print('Main    : before running process')
    x.start()
    print('Main    : wait for the process to finish')
    # x.join()
    print('Main    : all done')