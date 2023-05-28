N = int(input())

if N % 1000 == 0:
    print(N % 1000)
else:
    print(1000 - N % 1000)