N, K = map(int, input().split(' '))

a = N

for i in range(K):
    g1 = sorted(list(str(a)), reverse=True)
    g1 = ''.join(g1)
    g1 = int(g1)

    g2 = sorted(list(str(a)))
    j = 0
    while g2[j] == 0:
        j += 1
    g2 = g2[j:]
    g2 = ''.join(g2)
    g2 = int(g2)

    f = g1 - g2

    a = f

print(a)
