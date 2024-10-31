N= int(input())
n=1
a=1
for i in range(N-1):
    print(" "*(N-a)+"*"*n)
    n+=2
    a+=1

print("*"*(2*N-1))

for i in range(N):
    n-=2
    a-=1
    print(" "*(N-a)+"*"*n)