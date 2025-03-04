# SuperFastPython.com
# example of the submit and wait for first the ProcessPoolExecutor
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait
from concurrent.futures import FIRST_COMPLETED

# custom task that will sleep for a variable amount of time
def task(name):
    # sleep for less than a second
    sleep(random())
    return name

# entry point
def main():
    # start the process pool
    executor = ProcessPoolExecutor()
    # submit tasks and collect futures
    futures = [executor.submit(task, i) for i in range(10)]
    # wait until any task completes
    done, not_done = wait(futures, return_when=FIRST_COMPLETED)
    # get the result from the first task to complete
    print(done.pop().result())
    # shutdown without waiting
    executor.shutdown(wait=False, cancel_futures=True)

if __name__ == '__main__':
    main()
