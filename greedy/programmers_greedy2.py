def solution(name):
    # 문자 바꾸기 횟수 상, 하
    ans = 0
    n = len(name)

    for i in name:
        if i == 'A':
            continue
        elif ord(i) - 65 < 13:   # 순차적으로 가는게 더 빠를 때
            ans += ord(i)-65
        else:
            ans += ord('Z') - ord(i) + 1  # 거꾸로 가는게 더 빠를 때

    # 커서 위치 바꾸기 횟수 좌, 우
    arr = []

    for j in name:        # 0, 1(A) 로 이루어진 리스트 선언
        if j == 'A':
            arr.append(1)
        else:
            arr.append(0)

    if arr.count(0) == n:  # A가 하나도 없으면 길이-1 만큼 더하고 바로 리턴
        ans += n-1
        return ans

    l_idx, r_idx = 0, 0  # left - , right +

    if arr[0] == 0:  # 첫 문자가 A가 아니라면 얘는 시작점이므로 1처리
        arr[0] = 1

    while arr.count(1) != n:
        l_idx -= 1
        r_idx += 1
        if arr[l_idx] != 1 or arr[r_idx] != 1:
            if -l_idx > r_idx:
                arr[r_idx] = 1
                ans += r_idx
                l_idx = r_idx
            else:
                arr[l_idx] = 1
                ans += -l_idx
                r_idx = l_idx

    return ans


name = "JAZ"

print(solution(name))

# 총 26개의 알파벳
# A = 65
