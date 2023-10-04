def main():
    N, M = list(map(int, input().split()))
    cost_cell = []
    for _ in range(N):
        cost_cell.append(list(map(int, input().split())))
    
    dp = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                dp[i][j] = cost_cell[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + cost_cell[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + cost_cell[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + cost_cell[i][j]
    
    print(dp[N-1][M-1])
    
        
if __name__ == '__main__':
	main()
