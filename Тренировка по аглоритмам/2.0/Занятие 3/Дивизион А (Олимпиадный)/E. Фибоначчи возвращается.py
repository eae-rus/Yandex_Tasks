from decimal import Decimal

def main():
    '''
    '''
    N = int(input())

    A = [0] * N
    for i in range(N):
        A[i] = Decimal(input())
        
    max_number = max(A)
    set_Fibonacci = set()
    set_Fibonacci.add(1)
    
    Fibonacci_1 = 1
    Fibonacci_2 = 1
    while True:
        Fibonacci_2, Fibonacci_1 = Fibonacci_2 + Fibonacci_1, Fibonacci_2
        set_Fibonacci.add(Fibonacci_2)
        if Fibonacci_2 > max_number:
            break
    
    for i in range(len(A)):
        if A[i] in set_Fibonacci:
            print('Yes')
        else:
            print('No')
    
if __name__ == '__main__':
	main()