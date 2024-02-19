from .. import celery_app


celery_app.task
def computeFibonacciTask(n):
    if n <= 1:
        return n
    else:
        return computeFibonacciTask(n - 1) + computeFibonacciTask(n - 2)
