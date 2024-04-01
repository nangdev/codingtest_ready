def solution(phone_book):
    lenarr = []

    for i in phone_book:
        lenarr.append(len(i))
    
    idx = lenarr.index(min(lenarr))