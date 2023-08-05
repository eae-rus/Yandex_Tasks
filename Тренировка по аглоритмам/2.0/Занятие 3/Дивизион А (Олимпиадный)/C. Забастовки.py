def main():
    '''
    '''
    N, K = list(map(int, input().split()))

    days_off = set()
    for _ in range(6, N+1, 7):
        days_off.add(_)
    for _ in range(7, N+1, 7):
        days_off.add(_)
        
    all_strikes = set()
    for _ in range(K):
        a, b = list(map(int, input().split()))

        for i in range(a, N+1, b):
            if i in days_off or i in all_strikes:
                continue
            
            all_strikes.add(i)
    
    print(len(all_strikes))  
    
if __name__ == '__main__':
	main()