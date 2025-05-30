'''
Write a recursive function sum_digits(n) that returns the sum of the digits of a non-negative integer n.

Ex.
sum_digits(123) → 6     # because 1 + 2 + 3 = 6
sum_digits(0)   → 0
sum_digits(9)   → 9
sum_digits(1001) → 2    # 1 + 0 + 0 + 1 = 2

Completed in 24 mins 13 secs
'''

def sum_digits(n):
    
    if n == 0:
        return 0
    
    # n % 10 gives the last digit, so if n = 123, you get 3
    # n // 10 removes last digit, so if n = 123 you get 12
    # and then you get 2 and 1 and then finally 2 and 1 are added, and then 3 is added to that
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(123))