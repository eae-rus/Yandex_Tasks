def main():
    '''
    '''
    N, K = list(map(int, input().split()))

    all_strikes = set()
    for _ in range(K):
        a, b = list(map(int, input().split()))
        
        # Закоментил. Но в условии не сказано, что нужно выводить только те дни
        # когда наносится финансовый ущерб.
        #for i in range(a, N+1, b):
        #    all_strikes.add(i)

        for i in range(a, N+1, b):
            if i % 6 != 0 and i % 7 != 0:
                all_strikes.add(i)
    
    print(len(all_strikes))  
    
if __name__ == '__main__':
	main()