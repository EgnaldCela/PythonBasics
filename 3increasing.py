""" 2021/2022 exam """
def solution(V):
    n = len(V)
    for i in range(n):
        count = 0
        for j in range(i,n):
            if V[j] > V[i]:
                count += 1
            if count==3:
                return True
    return False

print(solution([11,10,70,50]))