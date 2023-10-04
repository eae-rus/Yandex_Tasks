def main():
    N, M = list(map(int, input().split()))
    cost_cell = []
    for _ in range(N):
        cost_cell.append(list(map(int, input().split())))
    
    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp_way = [["End" for _ in range(M)] for _ in range(N)] # 1 - D (вниз), 2 - R (вправо)
    
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                dp[i][j] = cost_cell[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + cost_cell[i][j]
                dp_way[i][j] = 'R'
            elif j == 0:
                dp[i][j] = dp[i-1][j] + cost_cell[i][j]
                dp_way[i][j] = "D"
            else:
                cost_way_1 = dp[i-1][j]
                cost_way_2 = dp[i][j-1]
                if cost_way_1 > cost_way_2:
                    dp[i][j] = cost_way_1 + cost_cell[i][j]
                    dp_way[i][j] = "D"
                else:
                    dp[i][j] = cost_way_2 + cost_cell[i][j]
                    dp_way[i][j] = "R"
    
    way = []                
    i, j = N-1, M-1
    dirrection = dp_way[N-1][M-1]
    while dirrection != "End":
        if dirrection == "D":
            way.append(dirrection)
            i -= 1
            dirrection = dp_way[i][j]
        else: # dirrection == R (вправо)
            way.append(dirrection)
            j -= 1
            dirrection = dp_way[i][j]
    
    
    print(dp[N-1][M-1])
    print(' '.join(way[::-1]))
    
        
if __name__ == '__main__':
	main()
