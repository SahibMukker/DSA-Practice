'''
Write a recursive function fibonacci(n) that returns the nth Fibonacci number.

The Fibonacci sequence is defined as:
fib(0) = 0
fib(1) = 1
For n > 1: fib(n) = fib(n-1) + fib(n-2)

Completed in 4 mins 13 secs, this code is intuitive but not efficient
but i havent learned how to do top-down or bottom-up dynamic programming yet so it gonna be like this for now
'''

def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    # recursively add the result of the two previous digits
    return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(4))