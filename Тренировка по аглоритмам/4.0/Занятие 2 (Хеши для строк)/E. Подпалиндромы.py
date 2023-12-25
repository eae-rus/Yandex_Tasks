def main():
    '''
    '''
    strings = input()
    
    N = len(strings)
    h_1 = [0] * (N + 1)
    h_2 = [0] * (N + 1)
    x = 27+1  # прописные латинские буквы
    degree_x = [1] * (N + 1)
    p = 1000000007
    
    for i in range(1, N + 1):
        index_char = ord(strings[i - 1]) - ord('a') + 1
        h_1[i] = (h_1[i - 1] * x + index_char) % p
       
        index_char = ord(strings[-i]) - ord('a') + 1
        h_2[i] = (h_2[i - 1] * x + index_char) % p

        degree_x[i] = degree_x[i-1] * x % p

    answer = N # по 1 символу
    
    for len_sub in range(2, 4): # длина подпалиндрома
        for ind in range(0, N+1-len_sub): # начало подпалиндрома
           if strings[ind] == strings[ind + len_sub - 1]:
                    answer += 1
    
    for len_sub in range(4, N+1): # длина подпалиндрома
        for ind in range(0, N+1-len_sub): # начало подпалиндрома
            #if (h_1[ind + len_sub] - h_1[ind] * degree_x[len_sub]) % p == (h_2[N - ind] - h_2[N - ind - len_sub] * degree_x[len_sub]) % p:
            h_1_sum = (h_1[ind + len_sub] + h_2[N - ind - len_sub] * degree_x[len_sub]) % p
            h_2_sum = (h_2[N - ind] + h_1[ind] * degree_x[len_sub]) % p
            if (h_1_sum == h_2_sum):
                 answer += 1
    
    print(answer)
    
if __name__ == '__main__':
	main()