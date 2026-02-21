S = list(input())
T = list(input())

flag = True

for i in T:
    if i in S:
        S.remove(i)
        continue
    else:
        print("NEED FIX")
        flag = False
        break

if flag:
    print("OK")

