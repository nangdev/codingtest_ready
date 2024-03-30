def solution(nums):
    ans = len(set(nums))
    
    if ans > len(nums)//2:
        return len(nums)//2
    else:
        return ans