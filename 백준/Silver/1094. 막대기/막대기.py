import heapq

hp = [64]

X = int(input())

stick = 64

while stick > X:
    shortest = heapq.heappop(hp)
    heapq.heappush(hp, shortest / 2)
    if sum(hp) < X:
        heapq.heappush(hp, shortest / 2)

    stick = sum(hp)

print(len(hp))