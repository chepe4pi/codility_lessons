def solution(A):
    A.sort()
    for num, i in enumerate(A):
        if i != num + 1:
            return num + 1


if __name__ == '__main__':
    assert solution([2, 3, 4, 6]) == 1
    assert solution([1, 3]) == 2
    assert solution([1, 2, 3, 4, 6]) == 5
    assert solution([1, 2, 3, 4, 4]) == 5
