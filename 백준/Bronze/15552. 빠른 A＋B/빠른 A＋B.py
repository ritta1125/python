import sys
input=sys.stdin.readline

a=int(input())

for i in range(a):
    x,y=map(int,input().split())
    print(x+y)