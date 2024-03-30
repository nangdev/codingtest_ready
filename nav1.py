def solution(plants, watered):
    result = []
    temp_plants = []
    N = len(plants)

    for i in plants:
        temp_plants.append(i)
    
    for w in watered:

        for tp in range(N):
            temp_plants[tp] -= 1
        
        if temp_plants[w-1] >= 0:
            temp_plants[w-1] = plants[w-1]
        
        count = 0
        for ans in temp_plants:
            if ans > 0:
                count += 1
        
        result.append(count)
    
    return result


print(solution([2,1,3,4,3], [2,2,2,2,5,5,5]))

# result = [4,2,2,2,2,1]

#[5,5,5] ,  [1,2,1,2,3]  == [3,3,3,3,3]

# [2,1,3,4,3] , [2,2,2,2,5,5,5] == [5,4,2,1,0,0,0]
