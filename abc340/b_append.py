Q = int(input())
A = []

for _ in range(Q):
    type, value = map(int, input().split())

    if(type == 1):
        A.append(value)
    elif (type == 2):
        print(A[-value])
    else:
        pass