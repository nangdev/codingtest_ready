tep = [1,2,3]
ans1 = [4,5,6]

ans = []

for i in zip(tep,ans1):
    ans.append(i)


for k in zip(*ans):
    print(k)