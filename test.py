
import timeit
import time




x = timeit.timeit() * 1000


y = (timeit.timeit() * 1000) - x
print(y)