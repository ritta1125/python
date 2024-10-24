N,M=map(int,input().split())
s=[]

for i in range(N):
    s.append(0)

for i in range(M):
    a,b,c=map(int,input().split())
    for j in range(a-1,b):
        s[j]=c

for i in range(N):
    print(s[i],end=" ")
