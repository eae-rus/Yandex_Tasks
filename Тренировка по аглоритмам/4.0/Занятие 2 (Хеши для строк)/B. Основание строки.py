def main():
    '''
    '''
    S = input()
    n = len(S)
    h = [0] * (n + 1)
    x = 27 # в теории, можно и 27, так как англлийские буквы
    degree_x = [1] * (len(S) + 1)
    p = 1000000007
    
    for i in range(1, n + 1):
        index_char = ord(S[i - 1]) - ord('a') + 1
        h[i] = (h[i - 1] * x + index_char) % p
        degree_x[i] = degree_x[i-1] * x % p
      
    for i in range(1, n + 1):
        if (S[0] == S[i]):
            L = n-i # len_substring
            h_suffix_prefix = (h[L] + h[i] * degree_x[L]) % p
            h_prefix_suffix = h[n]
            if (h_prefix_suffix == h_suffix_prefix):
                print(i)
                break
        
if __name__ == '__main__':
	main()