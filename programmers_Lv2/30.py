def solution(str1, str2):
    ar1, ar2 = [], []

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            st = str1[i].lower() + str1[i+1].lower()
            ar1.append(st)

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            st = str2[i].lower() + str2[i+1].lower()
            ar2.append(st)

    kyo = []
    hap = ar2[:]
    

    temp = ar2[:]
    temp2 = ar2[:]
    for k in ar1:
        if k in temp:
            kyo.append(k)
            temp.remove(k)

        if k not in temp2:
            hap.append(k)
        else:
            temp2.remove(k)

    jarkard = len(kyo) / len(hap) if len(hap) != 0 else 1

    return int(jarkard * 65536)


print(solution("FRANCE", "french"))
