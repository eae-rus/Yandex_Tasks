def main():
    '''
    '''
    N = int, input()
    A_list = list(map(int, input().split()))
    max_A = max(A_list)
    sum_A = sum(A_list)
    answer = 1
    if sum_A - 2*max_A == 0:
        answer = sum_A
    else:
        answer = 2*max_A - sum_A
    print(answer)    
    
    
if __name__ == '__main__':
	main()