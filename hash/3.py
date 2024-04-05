def solution(phone_book):
    p = sorted(phone_book)

    print(p)
    
    for i in range(len(phone_book)-1):
        if p[i+1].startswith(p[i]):
            return False
    
    return True


print(solution(["1212312", "123", "1235", "567", "88","1234","12"]))
