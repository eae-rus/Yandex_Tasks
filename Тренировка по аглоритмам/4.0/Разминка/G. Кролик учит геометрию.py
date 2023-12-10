def main():
    '''
    '''
    N, M = map(int, input().split())
    beds = []
    for _ in range(N):
        beds.append(list(map(int, input().split())))
    max_quared = 0
    quared_area = [[0 for _ in range(M)] for _ in range(N)]
    
    for row in range(N):
        for col in range(M):
            if (row == 0 or col == 0) and beds[row][col] == 1:
                quared_area[row][col] = 1
            elif beds[row][col] == 1:
                quared_area[row][col] = min(quared_area[row-1][col], quared_area[row][col-1], quared_area[row-1][col-1]) + 1
            max_quared = max(max_quared, quared_area[row][col])
    
    print(max_quared)            
            
if __name__ == '__main__':
	main()