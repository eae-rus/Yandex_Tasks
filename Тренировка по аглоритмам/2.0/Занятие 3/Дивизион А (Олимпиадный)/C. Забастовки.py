def main():
    '''
    '''
    N, K = list(map(int, input().split()))

    all_strikes = set()
    for _ in range(K):
        a, b = list(map(int, input().split()))

        for i in range(a, N+1, b):
            if i % 6 == 0 or i % 7 == 0 or i in all_strikes:
                continue
            
            all_strikes.add(i)
    
    print(len(all_strikes))  
    
if __name__ == '__main__':
	main()