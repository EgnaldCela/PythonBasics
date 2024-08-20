def longestSubsequence(string1, string2) -> int:
    m,n = len(string1), len(string2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m):
        for j in range(1,n):
            if string1[i] == string2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return max(max(i) for i in dp)

print(longestSubsequence("oxcpqrsvwf","shmtulqrypy"))