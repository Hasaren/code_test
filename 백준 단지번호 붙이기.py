# DFS

import sys

T = int(input())
M = []
for i in range(T):
    line = list(map(int, list(sys.stdin.readline())[:-1]))
    M.append(line)

def dfs(i1, j1):
    M[i1][j1] = 0
    visit[i1][j1] = 1
    nx = [0,0,1,-1]
    ny = [1,-1,0,0]
    for n in range(4):
        if (0<=i1+nx[n]<T) and (0<=j1+ny[n]<T) and (M[i1+nx[n]][j1+ny[n]] == 1):
            dfs(i1+nx[n],j1+ny[n])

S_l=[]
for i in range(T):
    for j in range(T):
        if M[i][j]==1:
            visit = [[0] * T for _ in range(T)]
            dfs(i, j)
            S = 0
            for v in visit:
                S += sum(v)
            S_l.append(S)
            # print(S_l)

print(len(S_l))

S_l.sort()
for s in S_l:
    print(s)