def solution(N):
    b_N = bin(N)[2:]
    if '0' not in b_N:
        return 0
    current_binary_gap = '0'
    while True:
        next_binary_gap = current_binary_gap + '0'
        if next_binary_gap not in b_N:
            return len(current_binary_gap)
        current_binary_gap = next_binary_gap

if __name__ == '__main__':
    assert solution(1000) == 3
    assert solution(17897) == 3
    assert solution(529) == 4
    assert solution(1041) == 5
