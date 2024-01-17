N = int(input("N: "))
M = int(input("M: "))

summ = 0
for i in range(N, M+1):
    summ += i

avg = summ / (M - N + 1)

print(summ, avg)