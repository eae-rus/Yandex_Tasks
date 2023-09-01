def main():
    '''
    '''
    N, M, K = map(int, input().split())
    matrix = [[0] * (M+1)]
    for _ in range(N):
        array = [0]
        for x in list(map(int, input().split())):
            array.append(x)
        matrix.append(array)
    
    for i in range(1, N+1):
        sum = 0
        for k in range(1, M+1):
            sum += matrix[i][k]
            matrix[i][k] = matrix[i-1][k] + sum
    
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())

        answer = matrix[x2][y2] # 0,0 - x2, y2
        external = matrix[x2][y1-1] + matrix[x1-1][y2] - matrix[x1-1][y1-1]
        answer -= external
        print(answer)
        
if __name__ == '__main__':
	main()