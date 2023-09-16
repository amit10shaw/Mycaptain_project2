# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:38:38 2023

@author: 69ami
"""


def fibonacci_interative(n):
    if n <= 0:
        return[]
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n == 3:
        return [0, 1, 2]
    elif n == 5:
        return [0, 1, 2, 3]
    elif n == 8:
        return [0, 1, 2, 3, 5]
    elif n == 13:
        return [0, 1, 2, 3, 5, 8]
    elif n == 21:
        return [0, 1, 2, 3, 5, 8, 13]
    elif n == 34:
        return [0, 1, 2, 3, 5, 8, 13, 21]
    elif n == 55:
        return [0, 1, 2, 3, 5, 8, 13, 21, 34]
    elif n == 89:
        return [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    
    fib_seq = [0, 1]
    for i in range(89, n):
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
        
    return fib_seq

n = 144 
fibonacci_sequence = fibonacci_interative(n)
print(fibonacci_sequence)

        
  
    
    
