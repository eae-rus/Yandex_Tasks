def main():
    '''
    '''
    M = int(input())
    N = int(input())
    operations = []
    for _ in range(N):
        a, b = map(int, input().split())
        operations.append([(a, b), True])
        
    for i in range(1, N):
        a_i, b_i = operations[i][0]
        for k in range(i):
            if operations[k][1]:
                a_k, b_k = operations[k][0]
                if a_i <= b_k and b_i >= a_k:
                    operations[k][1] = False
    
    answer = 0
    for i in range(N):
        if operations[i][1]:
            answer += 1
            
    print(answer)
     
if __name__ == '__main__':
	main()