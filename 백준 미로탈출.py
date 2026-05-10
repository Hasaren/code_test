# BFS
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline()[:-1])))

# print(A)

def bfs(s):
    queue = deque([s])
    # cnt = 0
    nx = [0,0,-1,1]
    ny = [-1,1,0,0]
    # A[s[0]][s[1]] = 0
    while queue:
        v = queue.popleft()
        # cnt += 1
        # if (N-1,M-1) in v:
        #     break

        # line = []
        # for l in v:
        for ni, nj in zip(nx,ny):
            if (0<=v[0]+ni<N) and (0<=v[1]+nj<M) and (A[v[0]+ni][v[1]+nj] == 1):
                A[v[0] + ni][v[1] + nj] = A[v[0]][v[1]]+1
                queue.append((v[0] + ni, v[1] + nj))
                # line.append((l[0] + ni, l[1] + nj))

        # if len(line) > 0:
        #     queue.append(line)

    # print("end")
    return A[N-1][M-1]
re = bfs((0,0))
print(re)