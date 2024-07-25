# import sys
# sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
arr = [input() for _ in range(n)]

# ACGT 미리 사전순 등록

hd = [[0, 0, 0, 0] for _ in range(m)]

for dna in arr:
    for c in range(m):
        if dna[c] == 'A':
            hd[c][0] += 1
        elif dna[c] == 'C':
            hd[c][1] += 1
        elif dna[c] == 'G':
            hd[c][2] += 1
        else:
            hd[c][3] += 1

ans = ""

for h in hd:
    val = h.index(max(h))

    if val == 0:
        ans += 'A'
    elif val == 1:
        ans += 'C'
    elif val == 2:
        ans += 'G'
    else:
        ans += 'T'

key = 0

for dna in arr:
    for i in range(m):
        if ans[i] != dna[i]:
            key += 1

print(ans)
print(key)
