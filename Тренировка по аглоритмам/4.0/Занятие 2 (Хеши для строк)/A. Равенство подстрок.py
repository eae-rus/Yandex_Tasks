def main():
    '''
    '''
    S = input()
    h = [0] * (len(S) + 1)
    x = 27 # в теории, можно и 27, так как англлийские буквы
    degree_x = [1] * (len(S) + 1)
    p = 1000000007
    
    for i in range(1, len(S) + 1):
        index_char = ord(S[i - 1]) - ord('a') + 1
        h[i] = (h[i - 1] * x + index_char) % p
        degree_x[i] = degree_x[i-1] * x
    
    Q = int(input())
    for _ in range(Q):
        s_len, start_1, start_2 = map(int, input().split())
        if ( (h[start_1 + s_len] + h[start_2] * degree_x[s_len]) % p ==
             (h[start_2 + s_len] + h[start_1] * degree_x[s_len]) % p):
            print('yes')
        else:
            print('no')
        
        
if __name__ == '__main__':
	main()