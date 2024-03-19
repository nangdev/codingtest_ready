def solution(elements):
    e2 = elements + elements[:-1]
    temp = set()

    n = len(set(elements))
    N = len(elements)

    val = 0

    for i in range(N):
        val = elements[i]
        temp.add(val)
        for j in range(i+1, i+N):
            val += e2[j]
            temp.add(val)

    return len(temp)
