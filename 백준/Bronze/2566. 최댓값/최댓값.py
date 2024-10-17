number=[]
for i in range(9):
    a=list(map(int, input().split()))
    number.append(a)

m=number[0][0]
row=0
column=0
for i in range(len(number)):
    for j in range(len(number[0])):
        if number[i][j]>=m:
            m=number[i][j]
            row=i+1
            column=j+1

print(m)
print(row, column)