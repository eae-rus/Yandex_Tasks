def main():
    '''
    '''
    N, M, K = map(int, input().split())
    matrix = []
    for _ in range(N):
        array = [0]
        for x in list(map(int, input().split())):
            array.append(array[-1] + x)
        matrix.append(array)
    
    
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        x1, x2 = x1-1, x2-1
        
        answer = 0
        for x in range(x1, x2+1):
            answer += matrix[x][y2] - matrix[x][y1-1]

        print(answer)
        
if __name__ == '__main__':
	main()