def solution(new_id):
    answer = first(new_id)
    answer = second(answer)
    answer = third(answer)
    answer = fourth(answer)
    answer = fifth(answer)
    answer = sixth(answer)
    answer = seventh(answer)
    return answer


def first(new1):
    return new1.lower()


def second(new2):
    ans = ''
    for i in new2:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            ans += i

    return ans


def third(new3):
    nnew3 = new3 + 'a'
    ans = ''

    for i in range(len(new3)):
        if nnew3[i] == '.' and nnew3[i+1] == '.':
            continue
        else:
            ans += nnew3[i]

    return ans


def fourth(new4):
    return new4.strip('.')


def fifth(new5):
    if new5 == "":
        return 'a'
    else:
        return new5


def sixth(new6):
    ans = ''
    if len(new6) > 15:
        ans = new6[:15] if new6[14] != '.' else new6[:14]

    else:
        return new6

    return ans


def seventh(new7):
    ans = new7
    while (len(ans) < 3):
        ans += new7[-1]

    return ans


print(solution("abcdefghijklmn.p"))
