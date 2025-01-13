

"""simple function """

# 1: convert min to sec

def seconds(min):
    result = 60 * min
    return result

# 2: # formula for sphere volume: 4/3 * pi * r^3, r = radius

from math import pi
def sphere(r):
    return 4/3 * pi * r ** 3    

# 3: By the Pythagorean theorem, c = sqrt a^2 + b^2
#  calculate the length of hyp (c)

from math import sqrt
def hypotenues(a, b):
    return sqrt(a ** 2 + b ** 2)


# 4: Simple functions

def foo_1(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    elif n == 0:
        return "Zero"
    else:
        return n


# 5: Simple function

def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n




"""calling functions"""

# 1
print(seconds(2))

# 2
print(sphere(3))

# 3
print(hypotenues(3,4))

# 4
print(foo_1(-7))

# 5
print(fizz_buzz(30))
print(fizz_buzz(9))
print(fizz_buzz(20))
print(fizz_buzz(7))
