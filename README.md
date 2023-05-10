This decorator is used to **calculate time** required to perform function, to use this:

1.  Download **benchhmark.py** to working directory.
2.  add in the top of your file: ``from benchmark import time_decorator``
3.  Use it as ``@time_decorator``

Example:

``main.py``
```
from benchmark import time_decorator

@time_decorator
def calculate_something():
  sum = 0
  for i in range(0, 10_000_000):
    sum += 1
  return sum


print(calculate_something())
```
