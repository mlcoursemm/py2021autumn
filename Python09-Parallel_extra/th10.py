import concurrent.futures
import queue
import threading
import time

def producer(queue, event):
    print(f"Producer will write to queue... event.is_set() = {event.is_set()}")
    for i in range(10):
        print(f'Producer writing... {9-i}')
        time.sleep(0.5)
        queue.put(i*i)
    event.set()
    print(f"Producer sent event. Exiting / event.is_set() = {event.is_set()}")

def consumer(queue, event):
    print(f"Consumer is waiting for event... event.is_set() = {event.is_set()}")
    event.wait()
    print(f"Consumer received event! event.is_set() = {event.is_set()}")
    while not queue.empty():
        num = queue.get()
        print(f"Consumer got num: {num} (remain qsize={queue.qsize()})")
    event.clear()
    print(f"Consumer cleared event. Exiting  / event.is_set() = {event.is_set()}")

if __name__ == "__main__":
    pipeline = queue.Queue(maxsize=100)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
    print(f"Main: event.is_set() = {event.is_set()}")