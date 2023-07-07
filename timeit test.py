# testing timeit()
import timeit

# code snippet to be executed only once
mysetup = "5+5"

print(timeit.timeit(mysetup))