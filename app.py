'''
Days_5
Objective
In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.

Given an integer,
print its first multiples. Each multiple (where ) should be printed on a new line in the form: n x i = result.
'''
from pip._vendor.distlib.compat import raw_input


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
#runner_up()

'''
Task
Given a string, , of length that is indexed from to , print its even-indexed and odd-indexed characters as
space-separated strings on a single line (see the Sample below for more detail).

'''

def string_sperate():
    #reomve_Enter your string number:
    num = int(input('Enter your string number: '))
    for i in range(1, num+1):
        user_string = input('Enter your string')
        even_char = []
        odd_char = []
        for i in range(len(user_string)):
            if i%2 == 0:
                even_char.append(user_string[i])
            else:
                odd_char.append(user_string[i])
        print(''.join(even_char), ''.join(odd_char))

#string_sperate()

'''
# Day 7: Arrays

# Task 
# Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

# Input Format
# The first line contains an integer, N (the size of our array). 
# The second line contains N space-separated integers describing array A's elements.

# Constraints
# 1 <= N <= 1000
# 1 <= Ai <= 10000, where Ai is the ith integer in the array
# Output Format
# Print the elements of array A in reverse order as a single line of space-separated numbers.
'''
def reverse_order():

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(" ".join(str(x) for x in arr[::-1]))
#reverse_order()

class Person(object):

    age = 0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print ("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print ("You are young.")
        elif self.age >= 13 and self.age < 18:
            print ("You are a teenager.")
        else:
            print ("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


