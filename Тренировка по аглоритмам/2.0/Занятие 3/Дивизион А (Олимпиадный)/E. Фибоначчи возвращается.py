def main():
    '''
    '''
    def add_Fibonacci(list_Fibonacci, set_Fibonacci, max_number):
        while True:
            list_Fibonacci.append(list_Fibonacci[-1] + list_Fibonacci[-2])
            set_Fibonacci.add(list_Fibonacci[-1])
            if list_Fibonacci[-1] > max_number:
                break
        return (list_Fibonacci, set_Fibonacci)
        
    N = int(input())

    list_Fibonacci = []
    list_Fibonacci.append(1)
    list_Fibonacci.append(1)
    
    set_Fibonacci = set(list_Fibonacci)

    for _ in range(N):
        number = int(input())
        if number > list_Fibonacci[-1]:
            list_Fibonacci, set_Fibonacci = add_Fibonacci(list_Fibonacci, set_Fibonacci, number)

        if number in set_Fibonacci:
            print('YES')
        else:
            print('NO')
    
if __name__ == '__main__':
	main()