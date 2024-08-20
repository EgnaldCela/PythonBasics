# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:33:13 2024

@author: USER
"""

''' Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum. 
 
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23. '''
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [None]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = nums[i] + max(0,dp[i-1])
        return max(dp)
    
if __name__ == "__main__":
    test = Solution()
    print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
 
 