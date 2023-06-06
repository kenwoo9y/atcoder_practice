# 2で割れる回数を求める
def break_number(i):
    counter = 0

    while i >= 2:
        if i % 2 == 0:
            i //= 2
            counter += 1
        else:
            break
    
    return counter


N = int(input())

max = 0
result = 0

for i in range(1, N + 1):
    if break_number(i) >= max:
        max = break_number(i)
        result = i

print(result)