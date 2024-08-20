def longestSubstring(string1, string2) -> int:
    m,n = len(string1), len(string2)
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if string1[i] == string2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
    return max(max(i) for i in dp)

if __name__ == "__main__":
    print(longestSubstring("hello", "yelli"))

