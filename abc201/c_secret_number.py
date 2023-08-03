S = input()

counter = 0

# 0000~9999まで全探索
for i in range(10000):
    # 4桁の文字列を生成
    now = str(i).zfill(4)

    # 候補かどうかを判定するフラグ
    flag = True

    for i in range(10):
        if S[i] == 'o':
            # iが含まれていない場合は不適
            if str(i) not in now:
                flag = False
        
        if S[i] == 'x':
            # iが含まれていた場合は不適
            if str(i) in now:
                flag = False
    
    if flag:
        counter += 1

print(counter)
