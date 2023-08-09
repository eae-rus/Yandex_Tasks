def main():
    '''
    '''
    N = int(input())

    A = [0] * N
    for i in range(N):
        A[i] = int(input())
        
    max_number = max(A)
    
    list_Fibonacci = []
    list_Fibonacci.append(1)
    list_Fibonacci.append(1)
    while True:
        list_Fibonacci.append(list_Fibonacci[-1] + list_Fibonacci[-2])
        if list_Fibonacci[-1] > max_number:
            break
    
    set_Fibonacci = set(list_Fibonacci)
    
    for i in range(len(A)):
        if A[i] in set_Fibonacci:
            print('Yes')
        else:
            print('No')
    
if __name__ == '__main__':
	main()