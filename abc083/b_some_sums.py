# 各桁の和を算出する
def sum_digits(n) :
    sum = 0

    while n > 0 :
        sum += n % 10
        n //= 10
    
    return sum

N, A, B = map(int, input().split())

result = 0

for i in range(1, N + 1) :
    if A <= sum_digits(i) <= B :
        result += i
    
print(result)