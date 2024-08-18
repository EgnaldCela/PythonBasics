# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:41:15 2024

@author: Egnald Çela
"""
"""
Write the following function that could be used as a sorting key:
To order a list of strings ignoring the case, then in lexicographical order:
['bar', 'cat', 'Cat', 'car'] -> ['bar', 'car', 'Cat', 'cat']
"""
def ex1(l:list) -> list:
    return sorted(l, key = lambda x: (x.lower(), x))
l1 = ['bar', 'cat', 'Cat', 'car']

"""
To order a list of tuples of three integer positive elements considering 
the second element, then the first and finally the third:
[(1,5,6), (3,4,9), (1,1,1)] -> [(1,1,1), (3,4,9), (1,5,6)]
"""
def ex2(l2: list) -> list:
    return sorted(l2, key = lambda x: (x[1], x[0], x[2]))
l2 = [(1,5,6), (3,4,9), (1,1,1)]
"""
To order a list of strings, considering the number of characters in 
increasing order, then the ending letter, then the lexicographical order:
['snake', 'caterpillar', 'rat', 'bat', 'dog'] ->
 ['dog', 'bat', 'rat', 'snake', 'caterpillar']
"""
def ex3(l3: list) -> list:
    return sorted(l3, key = lambda x: (len(x), x[-1], x[0]))
l3 = ['snake', 'caterpillar', 'rat', 'bat', 'dog']
"""
To order a list of strings considering the number of 
vowels in decreasing order, then the whole length in
 increasing order, then the reverse alphabetical order.
['pear', 'peach', 'apple', 'banana', 'avocado'] ->
 ['avocado', 'banana', 'pear', 'peach', 'apple']

"""
def vowels_number(word:str) -> int:
    vowels = "aeiou"
    result =  0
    for char in word:
        if char in vowels:
            result += 1
    return result
def ex4(l4:list) -> list:
    return sorted(l4, key= lambda x: (vowels_number(x), -len(x), x[0]), reverse=True)
l4 = ['pear', 'peach', 'apple', 'banana', 'avocado']
"""
To order a list of positive integers so that the
odd numbers appear before the even numbers and the odd numbers 
are in increasing order, while the even numbers are in decreasing order.
[1,5,2,6,7,4,5,3,8] -> [1,3,5,5,7,8,6,4,2] 
"""
def helper(number:int):
    if number % 2 == 0: #even
        return (1, -number)
    else:
        return (0, number)
    
def ex5( l5:list) -> list:
    return sorted(l5, key = lambda x: helper(x))
                  
l5 = [1,5,2,6,7,4,5,3,8]