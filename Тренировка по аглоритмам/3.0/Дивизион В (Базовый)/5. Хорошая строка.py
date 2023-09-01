def main():
    '''
    '''
    N = int(input())
    symbols = [0] * (26+1)
    for i in range(N):
        count_symbol = int(input())
        symbols[i] = count_symbol
    
    answer = 0
    for i in range(N):
        if symbols[i+1] > symbols[i]:
            answer += symbols[i]
        else:
            answer += symbols[i+1]
    
    print(answer)
     
if __name__ == '__main__':
	main()