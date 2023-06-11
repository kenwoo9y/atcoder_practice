N, K  = map(int, input().split())
l = list(map(int, input().split()))

l.sort(reverse=True)
max_length = 0

for i in range(K):
    max_length += l[i]

print(max_length)