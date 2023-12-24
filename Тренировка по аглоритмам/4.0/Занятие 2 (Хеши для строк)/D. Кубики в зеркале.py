def main():
    '''
    '''
    N, M = map(int, input().split())
    cubes = list(map(int, input().split()))
    
    h_1 = [0] * (N + 1)
    h_2 = [0] * (N + 1)
    x = 1000000 + 1  # 1 ≤ M ≤ 1000000
    degree_x = [1] * (N + 1)
    p = 1000000007
    
    # FIXME: Можно сделать на половину длины, чтобы сравнивать с обратной кривой
    for i in range(1, N + 1):
        index_char = cubes[i - 1]
        h_1[i] = (h_1[i - 1] * x + index_char) % p
       
        index_char = cubes[-i]
        h_2[i] = (h_2[i - 1] * x + index_char) % p

        degree_x[i] = degree_x[i-1] * x % p

    answer = []
    start_i =  N // 2 + N % 2
    for i in range(start_i, N):
        if (cubes[i-1] == cubes[i]):
            h_sum_1 = h_1[N] + h_2[i] * degree_x[N]
            h_sum_2 = h_2[N] + h_1[i] * degree_x[N]
            if (h_sum_1 == h_sum_2):
                answer.append(i)
    answer.append(N)
    
    print(" ".join(map(str, answer)))
    
if __name__ == '__main__':
	main()