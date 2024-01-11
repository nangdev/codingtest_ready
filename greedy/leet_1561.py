piles = [2,4,1,2,7,8]

piles.sort()
ans = 0
print(piles)
for i in range(len(piles)//3):
    piles.pop(-1)
    ans += piles[-1]
    piles.pop(-1)

