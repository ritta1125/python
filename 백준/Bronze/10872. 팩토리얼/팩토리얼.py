def fac(N):
    result=1
    for i in range(N):
        result=result*(i+1)
    return result

print(fac(int(input())))
