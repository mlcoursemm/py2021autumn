import concurrent.futures
import multiprocessing
import time
import logging

def print_proc(mes):
    name = multiprocessing.current_process().name
    print(f'Process {name}: {mes}')
    
def producer(pipe):
    print_proc(f"Producer will write to queue...")
    for i in range(10):
        print_proc(f'Producer writing... {i}*{i}')
        time.sleep(0.5)
        pipe.send(i*i)
    print_proc(f'Producer writing... DONE')
    pipe.send('DONE')
    pipe.close()
    print_proc(f"Producer finishing.")

def consumer(pipe):
    print_proc(f"Consumer is waiting for event...")
    while True:
        mes = pipe.recv()
        print_proc(f"Consumer got: {mes}")
        if mes == 'DONE':
            break
    pipe.close()
    print_proc(f"Consumer finishing")

if __name__ == "__main__":
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    pipe_cons, pipe_prod = multiprocessing.Pipe()
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipe_prod)
        executor.submit(consumer, pipe_cons)
    print_proc(f"All is done")