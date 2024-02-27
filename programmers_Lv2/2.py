def solution(s):
    ans = ""
    count = 0
    for i in range(len(s)):
        if i == 0:
            if s[i].isdigit():
                ans += s[i]
            else:
                ans += s[i].upper()
            continue

        
        if s[i] == " ":
            count = 1
            ans += " "
            continue

        if count == 1:
            count = 0
            if s[i].isdigit():
                ans += s[i]
                
            else:
                ans += s[i].upper()
                
        else:
            ans += s[i].lower()

    return ans


print(solution("3people unFollowed me"))
