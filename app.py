'''
Days_5
Objective
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

Given an integer,
print its first multiples. Each multiple (where ) should be printed on a new line in the form: n x i = result.
'''

def multiples_each(n):

    for i in range(1,11):
        result = n*i
        print(f'{n} x {i} = {result}')

multiples_each(2)