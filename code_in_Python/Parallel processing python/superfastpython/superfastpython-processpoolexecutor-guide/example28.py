# SuperFastPython.com
# add a callback option to a future object
from time import sleep
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait

# callback function to call when a task is completed
def custom_callback(future):
    print('Custom callback was called', flush=True)

# mock task that will sleep for a moment
def work():
    sleep(1)
    print('Task is done')

# entry point
def main():
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # execute the task
        future = executor.submit(work)
        # add the custom callback
        future.add_done_callback(custom_callback)
        # wait for the task to complete
        wait([future])

if __name__ == '__main__':
    main()
