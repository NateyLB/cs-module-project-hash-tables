# Your code here
import math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    factorial_cache ={}
    def rec_factorial(n):
        if n == 0:
            return n
        elif n in factorial_cache:
            return factorial_cache[n]
        else:
            factorial_cache[n] = n * rec_factorial(n-1)
            return factorial_cache[n]
    pow_cache={}
    def rec_pow(x, y):
        if y <= 1:
            return x
        elif (x,y) in pow_cache:
            return pow_cache[(x,y)]
        else:
            pow_cache[(x,y)] = x * rec_pow(x, y-1)
        return pow_cache[(x,y)]    
    
    value = rec_pow(x,y)
    value //=(x + y)
    value %= 982451653
    return value





# Do not modify below this line!

# for i in range(50000):
#     x = random.randrange(2, 14)
#     y = random.randrange(3, 6)
#     print(f'{i}: {x},{y}: {slowfun(x, y)}')
# print(slowfun_too_slow(10,10))
print(slowfun(10,10))
