def solution(n):
    use = 0

    # 이동거리 역순으로 계산
    while n > 0:

        # 2로 나눠 나머지가 없다 -> 순간이동 한거임
        if n % 2 == 0:
            n //= 2

        # 나머지가 있다 -> 점프한거임
        else:
            n -= 1
            use += 1

    return use
