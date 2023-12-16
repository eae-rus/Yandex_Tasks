def main():
    '''
    '''
    S = input()
    h = [0] * (len(S) + 1)
    x = 257 # в теории, можно и 27, так как англлийские буквы
    for i in range(1, len(S) + 1):
        h[i] = (h[i - 1] * x + ord(S[i - 1])) % 1000000007
    
    Q = int(input())
    for _ in range(Q):
        s_len, A_start, B_start = map(int, input().split())
        h_A_B = (h[A_start + s_len] + h[B_start] * (x**s_len) ) % 1000000007
        h_B_A = (h[B_start + s_len] + h[A_start] * (x**s_len) ) % 1000000007
        if h_A_B == h_B_A:
            print('yes')
        else:
            print('no')
        
        
if __name__ == '__main__':
	main()