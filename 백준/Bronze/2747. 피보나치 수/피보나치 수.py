a=0
b=1
n=int(input())

if n<=2:
    print(1)
else:
    for i in range(n-1):
        res=a+b
        a=b
        b=res
    print(res)