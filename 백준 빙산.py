# DFS
import sys
sys.setrecursionlimit(10**4)
N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
# print(A)


nx = [0,0,1,-1]
ny = [1,-1,0,0]

def dfs(A, si, sj, visit, area):
    visit[si][sj] = False
    for ni, nj in zip(nx,ny):
        if (0<=si+ni<N) and (0<=sj+nj<M) and (A[si+ni][sj+nj] > 0) and visit[si+ni][sj+nj]:
            area += 1
            dfs(A, si+ni, sj+nj, visit, area)




# 시간의 흐름
T = 0
while True:
    visit = [[True] * M for _ in range(N)]
    t_A = [[0] * M for _ in range(N)]
    # 덩어리 확인
    all_a = []
    for i in range(N):
        for j in range(M):

            # tmp 판때기
            t_A[i][j] = A[i][j]
            if (A[i][j] > 0) and visit[i][j]:
                area = 1
                dfs(A, i, j, visit, area)
                all_a.append(area)
    # print(len(all_a))
    if len(all_a) >= 2:
        break

    melt = 0
    for a in A:
        melt += sum(a)
    if melt == 0:
        T = 0
        break


    # 바다 확인 -> 빙산 녹이기
    for i in range(N):
        for j in range(M):
            if t_A[i][j] > 0: # 빙산
                for ni, nj in zip(nx,ny):
                   if (0<=i+ni<N) and (0<=j+nj<M) and t_A[i+ni][j+nj] == 0:
                        A[i][j] -= 1
                A[i][j] = max(0, A[i][j])

    T += 1
print(T)