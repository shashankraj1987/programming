# SuperFastPython.com
from multiprocessing import get_all_start_methods
from multiprocessing import get_start_method
# list of all process start methods supported on the os
result = get_all_start_methods()
print(result)
# get the default process start method
result = get_start_method()
print(result)
