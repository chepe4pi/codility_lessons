def solution(A, K):
    to_return = A[-K:]
    to_return.extend(A[:-K])
    return to_return


if __name__ == '__main__':
    assert solution([3, 8, 9, 7, 6], 1) == [6, 3, 8, 9, 7]
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
