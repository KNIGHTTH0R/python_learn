import concurrent.futures
import time
import requests
import bs4
import os

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

def find_sum(num):
    sum_of_primes = 0

    ix = 2

    while ix <= num:
        if is_prime(ix):
            sum_of_primes += ix
        ix += 1

    return sum_of_primes

def sum_primes_thread(nums):
    with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
        for number, sum_res in zip(nums, executor.map(find_sum, nums)):
            print("{} : Sum = {}".format(number, sum_res))

def sum_primes_process(nums):
    with concurrent.futures.ProcessPoolExecutor(max_workers = 4) as executor:
        for number, sum_res in zip(nums, executor.map(find_sum, nums)):
            print("{} : Sum = {}".format(number, sum_res))

def load_url(current_url):
    print(os.getpid())
    res = requests.get(current_url)
    res.raise_for_status()

    current_page = bs4.BeautifulSoup(res.text,"html.parser")
    current_title = current_page.select('title')[0].getText()
    return current_title

def process_urls_thread_alt(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers = 4) as executor:
        future_to_url = {executor.submit(load_url, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print("{} : Url = {}".format(data, url))


def process_urls_process_alt(urls):
    with concurrent.futures.ProcessPoolExecutor(max_workers = 4) as executor:
        future_to_url = {executor.submit(load_url, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print("{} : Url = {}".format(data, url))

if __name__ == '__main__':
    nums = [100000, 200000, 300000]
    url_list = ["https://www.google.com", "https://www.ploggingdev.com/2016/11/beginning-python-3/", "https://www.ploggingdev.com/archive/", "https://www.ploggingdev.com/2016/11/data-types-in-python-3/", "https://www.ploggingdev.com/2016/11/strings-in-python-3/"]
    start = time.time()
    process_urls_process_alt(url_list)
    print("Time taken = {0:.5f}".format(time.time() - start))