# # DFS
# import sys
#
# s, d = map(int, sys.stdin.readline().split())
#
# # 0--수빈---동생
# # 0동생--수빈----
#
# result = []
# def dfs(start, cnt):
#     cnt += 1
#     if start == d:
#         result.append(cnt)
#         return
#
#     near = start
#     for i in [start-1, start+1, start*2]:
#         if (0<=i) and (abs(i-d) <= abs(near-d)):
#             near = i
#     dfs(near, cnt)
#
#
# cnt = 0
# dfs(s,cnt)
# print(result[0])

# BFS
import sys
from collections import deque

s, d = map(int, sys.stdin.readline().split())
visit = [True]*100001
def bfs(start, cnt):
    queue = deque([[start]])

    while queue:
        s = queue.popleft()
        for ss in s:
            visit[ss] = False
        cnt += 1
        if d in s:
            break

        line = []
        for l in s:
            for i in [l-1, l+1, l*2]:
                if (0 <= i <= 100000) and visit[i]:
                    visit[i] = False
                    line.append(i)
        if len(line) > 0:
            queue.append(line)
    return cnt


re = bfs(s,0)

print(re-1)