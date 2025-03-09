def primeChecker(n):
    nextPrime = n
    for i in range(2, int(nextPrime**0.5) + 1):
        if nextPrime % i == 0:
            return False
    return True

m = int(input())

for i in range(m):
    n = int(input())
    answer = n
    if answer == 0 or answer == 1:
        print("2")
        continue
    for j in range(n):
        if not primeChecker(answer):
            answer += 1
        else:
            print(answer)
            break