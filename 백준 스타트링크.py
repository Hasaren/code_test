# BFS
import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

visit=[True]*(F+1)

def bfs(start, cnt):
    queue = deque([[start]])

    while queue:
        s = queue.popleft()
        cnt += 1
        for ss in s:
            visit[ss] = False
        if G in s:
            return cnt-1

        line = []
        for ss in s:
            for i in [ss+U,ss-D]:
                if (1 <= i <= F) and (visit[i]):
                    visit[i] = False
                    line.append(i)
        if len(line) > 0:
            queue.append(line)

    return 'use the stairs'

re = bfs(S, 0)
print(re)