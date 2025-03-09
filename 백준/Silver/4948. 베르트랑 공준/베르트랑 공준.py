def primeChecker(n):
    prime = n
    for i in range(2, int(prime**0.5) + 1):
        if prime % i == 0:
            return False
    return True

n = 1

while True:
    n = int(input())
    if n == 0:
        break
    answer = n + 1
    count = 0
    for j in range(n):
        if primeChecker(answer):
            count += 1  
        answer += 1    
    print(count)