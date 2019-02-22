
def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


def factorial_recursive_tail(n, f=1):
    if n == 0:
        return f
    else:
        return factorial_recursive_tail(n-1, n*f)


print(factorial_iterative(23))
print(factorial_recursive(23))
print(factorial_recursive_tail(23))
