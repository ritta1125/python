total= int(input())
number= int(input())
Total=0

for i in range(number):
    a,b=map(int,input().split())
    Total+=a*b
    
if total==Total:
    print("Yes")
else:
    print("No")
