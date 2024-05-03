def solution(n, arr1, arr2):
    answer = []

    for num in range(n):
        tema = format(arr1[num],"b")
        if len(tema) < n:
            tema = "0"*(n-len(tema)) + tema
       
        temb = format(arr2[num], "b")
        if len(temb) < n:
            temb = "0"*(n-len(temb)) + temb
        
        anstemp = ""
        for i in range(n):
            if tema[i] == "1" or temb[i] == "1":
                anstemp += "1"
            else:
                anstemp += "0"
        
        ans = ""
        for an in anstemp:
            if an == "1":
                ans += "#"
            else:
                ans += " "
        
        answer.append(ans)
    return answer

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))