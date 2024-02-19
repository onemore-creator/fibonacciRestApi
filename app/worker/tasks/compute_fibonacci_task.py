from .. import celery_app
import gmpy2 

def _baseFibonacci(n):
    if n <= 1:
        return [n]
    
    fib_values = [gmpy2.mpz(0), gmpy2.mpz(1)]
    for i in range(2, n + 1):
        fib_values.append(gmpy2.mpz(fib_values[i - 1] + fib_values[i - 2]))
    
    return fib_values

@celery_app.task
def computeFibonacciTask(n):
    return str(_baseFibonacci(n)[n])

@celery_app.task
def computeFibonacciTaskReturnSequence(n):
    return list(map(lambda x : str(x), _baseFibonacci(n)))
