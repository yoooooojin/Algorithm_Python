from collections import deque

X, M = map(int, input().split())

power = X
q = deque([X])

for _ in range(1 if M == 1 else 2**M - 1):
    ancestor = q.popleft()

    kid1 = ancestor // 2
    kid2 = ancestor - kid1

    q.append(kid1)
    q.append(kid2)

    power += kid1
    power += kid2

print(power)