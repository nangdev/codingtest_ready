def solution(food_times, k):
    count = 0
    arlen = len(food_times)
    next_i = 0
    result = 0

    while count != k:
        if food_times[next_i] != 0:
            count += 1
            food_times[next_i] -= 1
            if next_i + 1 == arlen:
                next_i = 0
            else:
                next_i += 1
        
        else:
            if sum(food_times) == 0:
                return -1
            next_i += 1
    
    return next_i +1


print(solution([3, 1, 2], 5))
