# BFS
import sys
from collections import deque

T = int(input())
for _ in range(T):

    F = int(input())
    H = list(map(int, sys.stdin.readline().split()))

    F_l = deque([])
    for _ in range(F):
        F_l.append(list(map(int, sys.stdin.readline().split())))
    R = list(map(int, sys.stdin.readline().split()))
    F_l.append(R)


    def bfs(start):
        queue = deque([start])

        while queue:
            v = queue.popleft()

            if (abs(v[0]-R[0])+abs(v[1]-R[1])) <= 1000:
                return "happy"

            for _ in range(len(F_l)):
                vf = F_l.popleft()
                if (abs(v[0]-vf[0])+abs(v[1]-vf[1])) <= 1000:
                    queue.append(vf)
                else:
                    F_l.append(vf)
        return "sad"

    re = bfs(H)
    print(re)