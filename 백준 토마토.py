#BFS
import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
B=[]
for _ in range(H):
    l=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    B.append(l)
# print(B)

nx=[0,0,1,-1,0,0]
ny=[1,-1,0,0,0,0]
nz=[0,0,0,0,1,-1]

start=[]
for h in range(H):
    for n in range(N):
        for m in range(M):
            if B[h][n][m] == 1:
                start.append((h,n,m))

# print(start)
def bfs(graph, start):
    queue = deque([start])
    # for s in start:
    #     B[s[0]][s[1]][s[2]] = 1
    cnt = 0
    while queue:
        v = queue.popleft()
        # print(v)
        cnt += 1
        day=[]
        for vv in v:
            for n1, n2, n3 in zip(nx, ny, nz):
                if (0<=vv[0]+n1<H)and(0<=vv[1]+n2<N)and(0<=vv[2]+n3<M)and (graph[vv[0]+n1][vv[1]+n2][vv[2]+n3] == 0):
                    day.append((vv[0]+n1,vv[1]+n2,vv[2]+n3))
                    graph[vv[0] + n1][vv[1] + n2][vv[2] + n3] = 1
                # elif (0<=vv[0]+n1<H)and(0<=vv[1]+n2<N)and(0<=vv[2]+n3<M)and (graph[vv[0]+n1][vv[1]+n2][vv[2]+n3] == -1):
                #     graph[vv[0] + n1][vv[1] + n2][vv[2] + n3] = 1
        if len(day) > 0:
            queue.append(day)
    return cnt

re = bfs(B,start)

cnt = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if B[h][n][m] == 0:
                cnt+=1
if cnt == 0:
    print(re-1)
else:
    print(-1)