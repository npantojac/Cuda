import numpy as np
import math
from numba import vectorize
from timeit import default_timer as timer

x = np.arange(int(1e6))


npoints = int(1e6)
a = np.arange(npoints, dtype=np.float32)

@vectorize
def cpu_sqrt(x):
  return math.sqrt(x)


@vectorize(['float32(float32)'], target='cuda')
def gpu_sqrt(x):
    return math.sqrt(x)


start = timer()
np.sqrt(a)
print("Using ufunc:", timer() - start)


start = timer()
cpu_sqrt(a)
print("Using CPU:", timer() - start)

start = timer()
cpu_sqrt(a)
print("Using GPU:", timer() - start)

start = timer()
cpu_sqrt(a)
print("Using GPU:", timer() - start)