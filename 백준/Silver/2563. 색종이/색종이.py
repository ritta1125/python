area=[]
for i in range(100):
        area.append([0 for j in range(100)])

n= int(input())
for i in range(n):
    x, y=map(int,input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            area[j][k]=1

Area=0
for i in range(100):
    for j in range(100):
        if area[i][j]==1:
            Area+=1

print(Area)