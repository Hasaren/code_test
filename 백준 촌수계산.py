# DFS
import sys

M = int(input())
F = [[] for _ in range(M+1)]
a, b = map(int,sys.stdin.readline().split())
l = int(input())
for i in range(l):
    c, d = map(int, sys.stdin.readline().split())
    F[c].append(d)
    F[d].append(c)
# print(F)

visit = [False]*(M+1)
result = []
def dfs(ch, num):
    num+=1
    visit[ch]=True

    if ch == b:
        result.append(num)

    for i in F[ch]:
        if not visit[i]:
            dfs(i, num)

dfs(a,0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)

# visit=[0]*(M+1)
# opr1 = dfs(a)
# # print(visit)
# ar = sum(visit)
#
# visit=[0]*(M+1)
# opr2 = dfs(b)
# # print(visit)
# br = sum(visit)
#
# if a == b:
#     print(-1)
# else:
#     if opr1 == opr2:
#         print(ar+br)
#     else:
#         print(-1)