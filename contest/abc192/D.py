X = list(input())
M = int(input())

d = int(sorted(list(X), reverse=True)[0])

N = len(X)
n = d+1
cnt = 0

while True:
    if n**(N)>M:
        a = 0
        for i in range(N):
            a += n**(N-i-1) * int(X[i])
        if a <= M:
            cnt += 1
        else:
            break
    else:
        cnt += 1

    n += 1

print(cnt)
