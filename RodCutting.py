""" Given a rod of length n inches and an array of prices that includes prices of
all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces.
 For example, if the length of the rod is 8 and the values of different pieces are given as the following,
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) """


def solution(n):  # n -> length of rod
    A = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20}
    dp = [0] * (n + 1)
    for j in range(1, n + 1):
        max_val = 0
        for i in range(1, j + 1):
            max_val = max(max_val, A[i] + dp[j - i])
        dp[j] = max_val

    return dp[n]


print(solution(8))  # Expected output: 22
