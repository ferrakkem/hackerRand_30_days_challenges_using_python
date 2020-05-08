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

#multiples_each(2)

'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given scores. Store them in a list and find the score of the runner-up.
'''

def runner_up():
    n = int(input())
    arr = map(int, input().split())
    arr_set = set(arr)
    arr_list = list(arr_set)
    arr_list.sort(reverse=True)
    print(arr_list[1])
runner_up()