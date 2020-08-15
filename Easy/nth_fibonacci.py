# Nth Fibonacci

def getNthFibRec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)


def getNthFib(n, mem={1: 0, 2: 1}):
    if n in mem:
        return mem[n]
    else:
        mem[n] = getNthFib(n-1, mem) + getNthFib(n-2, mem)
        return mem[n]
