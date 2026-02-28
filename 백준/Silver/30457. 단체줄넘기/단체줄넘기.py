N = int(input())

student = list(map(int, input().split()))

count = 0

student.sort()
current = 0

for i in student[:]:
    if i > current:
        count += 1
        current = i
        student.remove(i)

current = 0

for i in student[:]:
    if i > current:
        count += 1
        current = i
        student.remove(i)

print(count)