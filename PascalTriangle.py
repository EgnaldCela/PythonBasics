# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:18:22 2024

@author: USER
"""

'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown '''
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        solution = [[1]]  # The first row is always [1]
        
        for number in range(1, numRows):
            previous_row = solution[number-1]
            current_row = [1] * (number + 1)
            
            for j in range(1, number):
                current_row[j] = previous_row[j-1] + previous_row[j]
            
            solution.append(current_row)
        
        return solution
    
if __name__ == "__main__":
    test = Solution()
    print(test.generate(10))





        
        