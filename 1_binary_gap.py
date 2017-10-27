def solution(N):
    b_N = bin(N)[2:]
    max_binary_gap = 0
    current_binary_gap = 0
    for i in b_N:
        if int(i) == 0:
            current_binary_gap += 1
            if current_binary_gap > max_binary_gap:
                max_binary_gap = current_binary_gap
        else:
            current_binary_gap = 0
    return max_binary_gap

if __name__ == '__main__':
    assert solution(1000) == 3
    assert solution(17897) == 3
    assert solution(529) == 4
    assert solution(1041) == 5
