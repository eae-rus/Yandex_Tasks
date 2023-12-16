def main():
    '''
    '''
    S = input()
    h = [0] * (len(S) + 1)
    x = 27 # в теории, можно и 27, так как англлийские буквы
    for i in range(1, len(S) + 1):
        index_char = ord(S[i - 1]) - ord('a') + 1
        h[i] = (h[i - 1] * x + index_char) % 1000000007
    degree_x = [1 for _ in range((len(S) + 1))]
    for i in range(1, len(S) + 1):
        degree_x[i] = degree_x[i-1] * x
    
    Q = int(input())
    for _ in range(Q):
        s_len, A_start, B_start = map(int, input().split())
        h_A_B = h[A_start + s_len] + h[B_start] * degree_x[s_len]
        h_B_A = h[B_start + s_len] + h[A_start] * degree_x[s_len]
        if h_A_B == h_B_A:
            print('yes')
        else:
            print('no')
        
        
if __name__ == '__main__':
	main()