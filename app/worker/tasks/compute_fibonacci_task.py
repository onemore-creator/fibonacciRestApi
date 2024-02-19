from .. import celery_app
import gmpy2 

@celery_app.task
def computeFibonacciTask(n):
    if n <= 1:
        return n
    
    fib_values = [gmpy2.mpz(0), gmpy2.mpz(1)]
    for i in range(2, n + 1):
        fib_values.append(gmpy2.mpz(fib_values[i - 1] + fib_values[i - 2]))

    return str(fib_values[n])
