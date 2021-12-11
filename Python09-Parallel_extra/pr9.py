import concurrent.futures
import multiprocessing
import time
import logging

def print_proc(mes):
    name = multiprocessing.current_process().name
    print(f'Process {name}: {mes}')
    
def producer(queue, event):
    print_proc(f"Producer will write to queue... event.is_set() = {event.is_set()}")
    for i in range(10):
        print_proc(f'Producer writing... {9-i}')
        time.sleep(0.5)
        queue.put(i*i)
    event.set()
    print_proc(f"Producer sent event. Exiting / event.is_set() = {event.is_set()}")

def consumer(queue, event):
    print_proc(f"Consumer is waiting for event... event.is_set() = {event.is_set()}")
    event.wait()
    print_proc(f"Consumer received event! event.is_set() = {event.is_set()}")
    while not queue.empty():
        num = queue.get()
        print_proc(f"Consumer got num: {num} (remain qsize={queue.qsize()})")
    event.clear()
    print_proc(f"Consumer cleared event. Exiting  / event.is_set() = {event.is_set()}")

if __name__ == "__main__":
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    manager = multiprocessing.Manager()
    pipeline = manager.Queue(maxsize=100)
    event = manager.Event()
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
    print_proc(f"Main: event.is_set() = {event.is_set()}")