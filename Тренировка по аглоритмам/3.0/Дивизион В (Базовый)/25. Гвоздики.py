def main():
    N = int(input())
    carnations = list(map(int, input().split()))
    carnations.sort()
    min_len_thread = [0] * N
    min_len_thread[0] = carnations[1] - carnations[0]
    min_len_thread[1] = min_len_thread[0]
    for i in range(2, N):
        min_len_thread[i] = min(min_len_thread[i-1], min_len_thread[i-2]) + carnations[i] - carnations[i-1]

        
    print(min_len_thread[-1])
    
        
if __name__ == '__main__':
	main()
