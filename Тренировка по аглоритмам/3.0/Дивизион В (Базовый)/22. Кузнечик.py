def main():
    N, K = list(map(int, input().split()))
    count_variant = [0] * N
    count_variant[0] = 1
    for i in range(0,N-1):
        for j in range(i+1, min(i+K+1, N)):
            count_variant[j] += count_variant[i]
    
    print(count_variant[-1])
        
if __name__ == '__main__':
	main()