import itertools
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
permutations = list(itertools.permutations(q, 4))
print(permutations)
def f(x):
    return x * 4 + 6

# Your code here

def sumdiff(a,b,c,d):
    if f(a) + f(b) == f(c) - f(b):
        # print("f({a}) + f({b}) = f({c)} - f({d})")
        print(f(a)," + ", f(b), " = ", f(c), " - ", f(d))

for variables in permutations:
    sumdiff(variables[0], variables[1], variables[2], variables[3])

