import timeit
from isEven import *

def benchmark(funcs,range=1000000000,number=1000000):
    setup = f"""
import random
num = random.randint(1, {range})
"""
    for i in funcs:
        print(f"{i.__name__} :")
        print(timeit.timeit(f"{i.__name__}(num)", setup=setup, number=number, globals=globals()))

benchmark([modulo,floatDivision,bitshiftXOR])
