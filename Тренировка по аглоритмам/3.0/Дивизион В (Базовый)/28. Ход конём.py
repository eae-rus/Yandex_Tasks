def main():
    N, M = list(map(int, input().split()))
  
    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp[0][0] = 1
    
    for i in range(N-1):
        for j in range(M-1):
            if dp[i][j] != 0:
                new_i = i + 1
                new_j = j + 2
                if new_i < N and new_j < M:
                    dp[new_i][new_j] += dp[i][j]
                
                new_i = i + 2
                new_j = j + 1
                if new_i < N and new_j < M:
                    dp[new_i][new_j] += dp[i][j]

    
    print(dp[N-1][M-1])
    
        
if __name__ == '__main__':
	main()
