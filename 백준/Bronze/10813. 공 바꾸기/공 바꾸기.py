N,M=map(int,input().split())
ball=[]

for i in range(N):
    ball.append(i+1)

for i in range(M):
    a,b=map(int,input().split())
    A=ball[a-1]
    B=ball[b-1]
    temp=A
    ball[a-1]=B
    ball[b-1]=temp

print(*ball)
