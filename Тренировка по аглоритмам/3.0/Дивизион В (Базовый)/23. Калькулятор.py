def main():
    N = int(input())
    count = 0
    array = [N]
    
    while N > 1:
        if N % 3 == 0:
            N = N // 3
            array.append(N)
        elif N % 2 == 0:
            N = N // 2
            array.append(N)
        else:
            N = N - 1
            array.append(N)
        count += 1
    
    print(count)
    print(' '.join(map(str, array[::-1])))
        
if __name__ == '__main__':
	main()