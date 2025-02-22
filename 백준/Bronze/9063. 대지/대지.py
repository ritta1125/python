X = []
Y = []
area = 0

count = int(input())

for i in range(count):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

area = (max(X) - min(X))*(max(Y) - min(Y))

print(area)
