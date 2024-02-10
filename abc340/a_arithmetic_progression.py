A,B,C = map(int, input().split())

x = range(A, B+1, C)
for i in x:
    print(i, end=" ")