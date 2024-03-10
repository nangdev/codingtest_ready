from collections import deque


def word_transformable(word1, word2):
    diff = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff += 1
        if diff > 1:
            return False
    return diff == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = set([begin])

    while queue:
        current_word, steps = queue.popleft()

        if current_word == target:
            return steps

        for word in words:
            if word not in visited and word_transformable(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0
