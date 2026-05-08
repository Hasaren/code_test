# DFS
import sys
from collections import deque

N, M, V= map(int, sys.stdin.readline().split())

A = [[] for _ in range(N+1)]
visit = [True]*(N+1)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)

def dfs(start,visit):
    visit[start] = False
    dfs_r.append(start)

    m = sorted(A[start])

    for mm in m:
        if visit[mm]:
            dfs(mm, visit)
            # break

dfs_r = []
dfs(V, visit)
# print(dfs_r)
for d in dfs_r:
    print(d, end=" ")
print()

# BFS
visit = [True]*(N+1)
def bfs(start, visit):
    queue = deque([start])
    visit[start] = False
    while queue:
        v = queue.popleft()
        bfs_r.append(v)
        m = sorted(A[v])
        for mm in m:
            if visit[mm]:
                queue.append(mm)
                visit[mm] = False



bfs_r = []
bfs(V, visit)
# print(bfs_r)
for b in bfs_r:
    print(b, end=" ")