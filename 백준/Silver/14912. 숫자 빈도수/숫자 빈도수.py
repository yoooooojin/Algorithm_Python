n, d = map(int, input().split())

lst = []
count = 0

for i in range(1, n+1):
    lst.extend(list(str(i)))

for i in lst:
    if i == str(d):
        count += 1

print(count)