# ??
import sys

N, M = map(int, sys.stdin.readline().split())
RC = list(map(int, sys.stdin.readline().split()))

R = []
for _ in range(N):
    R.append(list(map(int, sys.stdin.readline().split())))
# print(R)

def inarea(i, j):
    if 0<=i<N and 0<=j<M:
        return True
    else:
        return False


rot = [(-1,0),(0,1),(1,0),(0,-1)]


while True:
    if R[RC[0]][RC[1]] == 0:
        R[RC[0]][RC[1]] = 2 # 청소

    # 주변 체크
    cnt=0
    for i in rot:
        if R[RC[0]+i[0]][RC[1]+i[1]] == 0:
            cnt+=1
    if cnt > 0:
        # 반시계 90 회전
        RC[2] = (RC[2]-1)%4
        # print(RC[2])
        # 전방 확인
        if inarea(RC[0]+rot[RC[2]][0], RC[1]+rot[RC[2]][1]) and (R[RC[0]+rot[RC[2]][0]][RC[1]+rot[RC[2]][1]] == 0):
            # 전진
            RC = [RC[0]+rot[RC[2]][0],RC[1]+rot[RC[2]][1],RC[2]]
    else:
        # 후진 확인
        if inarea(RC[0]+rot[(RC[2]+2)%4][0], RC[1]+rot[(RC[2]+2)%4][1]) and (R[RC[0]+rot[(RC[2]+2)%4][0]][RC[1]+rot[(RC[2]+2)%4][1]] != 1):
            RC = [RC[0]+rot[(RC[2]+2)%4][0],RC[1]+rot[(RC[2]+2)%4][1],RC[2]]
        else:
            # print("종료")
            break

c_cnt = 0
for i in range(N):
    for j in range(M):
        if R[i][j] == 2:
            c_cnt+=1
print(c_cnt)