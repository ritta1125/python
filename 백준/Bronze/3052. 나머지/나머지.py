num=[]
res=[]

for i in range(10):
    num.append(int(input()))

for i in range(10):
    res.append(num[i]%42)

m= set(res)

print(len(m))
