import threading
from queue import Queue
import time
import zipfile
import random

list_lock = threading.Lock()

def find_rand(rand_num):
    while True:
        if is_prime(rand_num):
            with list_lock:
                prime_list.append(rand_num)
            break
        rand_num += 1

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True

def process_queue():
    while True:
        rand_num = min_nums.get()
        find_rand(rand_num)
        min_nums.task_done()

min_nums = Queue()

rand_list = [49674923266195, 64638487475080, 1161019450999, 11158231750939, 75626194509752]
prime_list = list()

for i in range(4):
    t = threading.Thread(target=process_queue)
    t.daemon = True
    t.start()

start = time.time()

for rand_num in rand_list:
    min_nums.put(rand_num)

min_nums.join()

prime_list.sort()
print(prime_list)

print("Execution time = {0:.5f}".format(time.time() - start))