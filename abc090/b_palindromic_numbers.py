def is_palindromic_numbers(i):
    reslut = False

    if str(i) == str(i)[::-1]:
        reslut = True

    return reslut


A, B = map(int, input().split())

counter = 0

for i in range(A, B + 1):
    if is_palindromic_numbers(i):
        counter += 1

print(counter)