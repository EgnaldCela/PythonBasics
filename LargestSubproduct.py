""" Taken from Algorithms 2022/2023 exam
 Let V be an array of n integers. If i, j are two integers such that 0</= i <= j <= n-1,
 then the p(i,j) product is defined as p(i,j) = V[i] * V[i+1] * V[i+2] ... V[j].
 Given an algorithm that returns the value of the larges p(i,j).
 Example: V=[1.5,4.0,2.0,0.1].
 The largest one is p(0,2) = 12.0"""


"""def solution(V):
    n = len(V)
    dp = [[1 for _ in range(n)] for _ in range(n)]
    dp[0][0] = V[0]
    current = -1
    for j in range(n):
        for i in range(j):
            dp[i][j] = dp[i][j-1] * V[j]
            if dp[i][j] > current:
                current = dp[i][j]
    return current """
""" The above implementation costs O(n^2).
We can do better than this. """
def solution(nums) -> int:
        dp = [None]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = nums[i] * max(1,dp[i-1])
        return max(dp)
print(solution([1.5,4.0,2.0,0.1]))
