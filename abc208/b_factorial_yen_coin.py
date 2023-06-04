from math import factorial

P = int(input())

coin = 0

for i in range(10, 0, -1):
    while P >= factorial(i):
        coin += 1
        P -= factorial(i)

print(coin)