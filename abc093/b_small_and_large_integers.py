A, B, K = map(int, input().split())

reslut = set()

for i in range(K):
    reslut.add(min(A + i, B))
    reslut.add(max(B - i, A))
        
# listにしてsortし、アンパックする
print(*sorted(list(reslut)), sep='\n')