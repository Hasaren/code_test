# # DFS
# import sys
#
# C = int(input())
# N = int(input())
#
# M = [[] for _ in range(C+1)]
# # print(M)
# for _ in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#     M[a].append(b)
#     M[b].append(a)
#
# # print(M)
#
# visit = [True]*(C+1)
# def dfs(s,visit):
#     visit[s] = False
#     for c in M[s]:
#         if visit[c]:
#             dfs(c,visit)
#
#
# dfs(1,visit)
#
# cnt = 0
# for v in visit:
#     if not v:
#         cnt+=1
# print(cnt-1)

# BFS
import sys
from collections import deque

C = int(input())
N = int(input())

M = [[] for _ in range(C+1)]
# print(M)
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    M[a].append(b)
    M[b].append(a)

# print(M)
visit = [True]*(C+1)

def bfs(s, visit):
    queue = deque([s])

    while queue:
        v = queue.popleft()
        visit[v] = False
        for c in M[v]:
            if visit[c]:
                visit[c] = False
                queue.append(c)

bfs(1,visit)

cnt = 0
for v in visit:
    if not v:
        cnt+=1
print(cnt-1)