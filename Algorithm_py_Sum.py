import math
#-------------------------------------
def sum_recursive(n):
    if n > 0:
        return n+sum_recursive(n-1)
    elif n < 0:
        return n+sum_recursive(n+1)
    else:
        return 0
#-------------------------------------
def sum_for(n):
    s = 0
    if n > 0:
        for i in range(1, n + 1):
            s = s + i
    elif n < 0:
        for i in range(n,1):
            s = s + i
    else:
        return 0
    return s
#-------------------------------------
def sum_Gauss(n):
    s = 0
    if n > 0:
        s = n*(n+1)//2 # in Python '//' double slash means integer divide
    elif n < 0:
        s = (n*(n-1)/2)*-1 # one slash will show ~.0
    else:
        return 0
    return s
#-------------------------------------

print("------sum recursive--------")
print("Sum = "+sum_recursive(10).__str__())
print("Sum = "+sum_recursive(-10).__str__())

print("------sum for--------")
print("Sum = "+sum_for(10).__str__())
print("Sum = "+sum_for(-10).__str__())

print("------sum Gauss--------")
print("Sum = "+sum_Gauss(10).__str__())
print("Sum = "+sum_Gauss(-10).__str__())

print("------Just Factorial--------")
print("Just Factorial "+math.factorial(5).__str__())

# # Result
# ------sum factorial--------
# Sum = 55
# Sum = -55
# ------sum for--------
# Sum = 55
# Sum = -55
# ------sum Gauss--------
# Sum = 55
# Sum = -55.0
# ------Just Factorial--------
# Just Factorial 120
