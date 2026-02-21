N, H, W = map(int, input().split())

lst = []
answer = ""

for _ in range(H):
    lst.append(list(input()))

for i in range(N):
    for j in range(H):
        for s in range(W*i, W*i+W):
            if lst[j][s] != '?' and len(answer) != i+1:
                answer += lst[j][s]
    if len(answer) != i+1:
        answer += '?'


print(answer)