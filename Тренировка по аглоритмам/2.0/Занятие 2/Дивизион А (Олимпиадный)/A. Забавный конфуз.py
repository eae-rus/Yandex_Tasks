def main():
    '''
    '''
    N, K = map(int, input().split())
    A_list = list(map(int, input().split()))
    max_A, min_A = max(A_list), min(A_list)
    diff = max_A - min_A
    print(diff)
    
if __name__ == '__main__':
	main()