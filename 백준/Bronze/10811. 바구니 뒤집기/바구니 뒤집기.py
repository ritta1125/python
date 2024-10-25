a,b=map(int,input().split())
S=[]

for i in range(a):
    S.append(i+1)

for i in range(b):
    x,y=map(int,input().split())
    c=S[x-1:y]
    c.reverse()
    S[x-1:y]=c

print(*S)
