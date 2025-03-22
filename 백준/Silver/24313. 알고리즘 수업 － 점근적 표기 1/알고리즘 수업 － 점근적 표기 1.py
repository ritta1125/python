a, b = map(int, input().split())
c = int(input())
n = int(input())

if b <= 0:
    if (c - a) * n >= 0:
        print("1")
    else:
        print("0")
else:
    if (c - a) * n >= 0:
        if b <= (c - a) * n:
            print("1")
        else:
            print("0")
    else:
        print("0")
