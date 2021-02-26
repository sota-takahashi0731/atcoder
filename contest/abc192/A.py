s = list(input())

for i in range(len(s)):
    if i%2==0:
        if s[i].isupper():
            print('No')
            exit()
    else:
        if s[i].islower():
            print('No')
            exit()

print('Yes')
