num=[]

for i in range(9):
    a=int(input())
    num.append(a)

b=max(num)
print(b)
print(num.index(b)+1)

