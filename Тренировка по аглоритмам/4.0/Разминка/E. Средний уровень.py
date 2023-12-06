def main():
    '''
    '''
    n = int(input())
    rating = list(map(int, input().split()))
    
    discontent_is_up = [0 for _ in range(n)]
    discontent_is_down = [0 for _ in range(n)]
    
    for i in range(1, n):
        discontent_is_up[i] = discontent_is_up[i - 1] + (rating[i] - rating[i - 1]) * i
        discontent_is_down[-1 - i] = discontent_is_down[-1 - i + 1] + (rating[-1 - i + 1] - rating[-1 - i]) * i
    
    # возможно не очень оптимально по памяти, можно было без новой переменной
    result = [x + y for x, y in zip(discontent_is_up, discontent_is_down)]

    print(" ".join(map(str,result)))
        
if __name__ == '__main__':
	main()