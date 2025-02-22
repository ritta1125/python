N = int(input())
a = 0
b = 0
notPrint =  False

for i in range(N):
    a = (N - i) // 5
    b = (N - 5 * a) // 3
    if (N - 5 * a) % 3 == 0:  
        print(a + b)
        notPrint = True
        break
    
if not notPrint:
	print(-1)