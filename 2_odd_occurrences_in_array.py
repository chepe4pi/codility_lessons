def solution(A):
    values_counts = {i: 0 for i in set(A)}
    for i in A:
        values_counts[i] += 1
    for key in values_counts.keys():
        if values_counts[key] == 1:
            return key


if __name__ == '__main__':
    print solution([1, 2, 3, 1, 2, 3, 4])
    assert solution([1, 2, 3, 1, 2, 3, 4]) == 4
    assert solution([4, 5, 6, 5, 6, 7, 7]) == 4
    assert solution([7, 8, 7, 9, 7, 8]) == 9
    assert solution([7, 8, 7, 7, 7, 8]) is None
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
