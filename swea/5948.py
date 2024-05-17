import sys
sys.stdin = open("input.txt",'r')

def dfs(n,cur,cnt):
    if n==7:
        if cnt == 3 and cur not in nums:
            nums.append(cur)
        return
    
    
    dfs(n+1,cur+arr[n],cnt+1)
    dfs(n+1,cur,cnt)

for t in range(1,int(input())+1):
    arr = list(map(int,input().split()))
    nums = []

    dfs(0,0,0)

    nums.sort(reverse=True)

    print(f"#{t} {nums[4]}")