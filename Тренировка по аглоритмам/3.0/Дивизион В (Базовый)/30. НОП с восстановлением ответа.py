def main():
    N = int(input())
    sequence_1 = list(map(int, input().split()))
    M = int(input())
    sequence_2 = list(map(int, input().split()))
    
    dp = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                if sequence_1[0] == sequence_2[0]:
                    dp[0][0] = 1
            elif i == 0:
                if dp[0][j-1] == 1:
                    dp[0][j] = 1
                elif sequence_1[0] == sequence_2[j]:
                    dp[0][j] = 1
            elif j == 0:
                if dp[i-1][0] == 1:
                    dp[i][0] = 1
                elif sequence_1[i] == sequence_2[0]:
                    dp[i][0] = 1
            else:
                if sequence_1[i] == sequence_2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
    subsequence = []
    i, j = N-1, M-1
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j-1] + 1:
            subsequence.append(sequence_1[i])
            i -= 1
            j -= 1
        elif i != 0 and dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1
    if i == 0 and dp[0][j] == 1:
        subsequence.append[sequence_1[0]]
    elif j == 0 and dp[i][0] == 1:
        subsequence.append[sequence_2[0]]
        
    subsequence.reverse()
            
    #print(dp[N-1][M-1])
    print(" ".join(map(str, subsequence)))
    
        
if __name__ == '__main__':
	main()
