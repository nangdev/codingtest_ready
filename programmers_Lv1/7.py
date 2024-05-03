def solution(board, moves):
    N = len(board)
    ans = 0
    stack = []

    for i in moves:
        i -= 1
        for jip in range(N):
            if board[jip][i]:
                val = board[jip][i]
                print(val)
                if stack:
                    if val == stack[-1]:
                        stack.pop()
                        ans += 2
                    else:
                        stack.append(val)
                else:
                    stack.append(val)

                board[jip][i] = 0
                break
    
    return ans


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
