# DFS
import sys
sys.setrecursionlimit(10**6)
N = int(input())

M = []
for _ in range(N):
    M.append(list(map(int, sys.stdin.readline().split())))


# 최대 높이 찾기
high = 0
for i in range(N):
    for j in range(N):
        if M[i][j] > high:
            high = M[i][j]

# print(high)



# 영역찾기
nx = [0,0,1,-1]
ny = [1,-1,0,0]
def dfs(visit, M1,M2,wh, area):
    visit[M1][M2] = 1
    for ni, nj in zip(nx,ny):
        if (0<=M1+ni<N) and (0<=M2+nj<N) and (M[M1+ni][M2+nj] > wh) and (visit[M1+ni][M2+nj]==0):
            area.append(1)
            visit[M1 + ni][M2 + nj] = 1
            dfs(visit, M1+ni, M2+nj, wh, area)


# 물검사 high-1까지 진행
all_c = []
for wh in range(high):
    t_M = [[0]*N for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N):
            if (M[i][j] > wh) and (t_M[i][j]==0):
                area = [1]
                dfs(t_M, i, j, wh, area)
                # print(sum(area))
                if sum(area) > 0:
                    result.append(sum(area))

    all_c.append(len(result))
print(max(all_c))