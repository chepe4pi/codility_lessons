def solution(A):
    P_list = []
    for i in xrange(1, len(A)):
        P_list.append(abs(sum(A[:i]) - sum(A[i:])))
    return min(P_list)


if __name__ == '__main__':
    assert solution([3, 1, 2, 4, 3]) == 1
    assert solution([3, 1]) == 2
