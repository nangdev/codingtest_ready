def solution(elements):
    e2 = elements + elements[:-1]
    temp = []

    n = len(set(elements))
    N = len(elements)

    val = 0

    for i in range(N):
        val = elements[i]
        for j in range(i+1,i+N):
            val += e2[j]
            temp.append(val)
    

    return len(set(temp))+n


print(solution([7,9,1,1,4]))