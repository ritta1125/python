N,M=map(int,input().split())
S=[]
s=[]

for r in range(N):
    A=list(map(int,input().split()))
    S.append(A)

for r in range(N):
    a=list(map(int,input().split()))
    s.append(a)

for r in range(N):
    for c in range(M):
        print(S[r][c]+s[r][c],end=" ")
    print()

