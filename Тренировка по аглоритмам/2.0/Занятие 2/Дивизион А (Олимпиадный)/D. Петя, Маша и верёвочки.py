def main():
    '''
    '''
    N = int, input()
    A_list = list(map(int, input().split()))
    max_A = max(A_list)
    sum_A = sum(A_list)
    answer = 1
    if 2*max_A - sum_A > 0:
        answer = 2*max_A - sum_A
    else:
        answer = sum_A
        
    print(answer)    
    
    
if __name__ == '__main__':
	main()