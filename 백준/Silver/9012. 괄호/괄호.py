n = int(input())

for i in range(n):
    stack = []
    a = input()
    isValid = True
    for p in a: 
        if p == "(":
            stack.append(p)
        else:
            if len(stack) == 0:
                isValid = False
                break
            else:
                stack.pop()
    if len(stack) > 0 or not isValid:
        print("NO")
    else:
        print("YES")
