def main():
    '''
    '''
    t = int(input())
    for _ in range(t):
        n, a, b = list(map(int, input().split()))
        is_real = True
        if a == b:
            if n % a != 0:
                is_real = False
        else:
            groups = n // a
            remains = n % a
            variance = b - a
            if remains // variance + 1 > groups:
                is_real = False
            
        if is_real:
            print('YES')
        else:
            print('NO')       
            
if __name__ == '__main__':
	main()