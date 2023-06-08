N = int(input())

list = []

for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    list.append([T, S])

list.sort(reverse=True)
print(list[1][1])