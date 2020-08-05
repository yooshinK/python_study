import math # more module info: docs.python.org/3/library/math.html
print(math.ceil(2.1)) # Result = 3
print(math.ceil(2.9)) # Result = 3
print(math.floor(2.1)) # Result = 2
print(math.floor(2.9)) # Result = 2
print(math.sqrt(15)) # Result = 3.872983346207417
print(3.872983346207417*3.872983346207417) # Result = 15.000000000000002

print("---------------------------------------")
import module_test2
def a():
    return 'bB'

print(a())
print(module_test2.a())
