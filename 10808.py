s = input()
li = [0]*26
for i in range(len(s)):
    x = ord(s[i])-97
    li[x] += 1
print(' '.join(map(str, li)))
