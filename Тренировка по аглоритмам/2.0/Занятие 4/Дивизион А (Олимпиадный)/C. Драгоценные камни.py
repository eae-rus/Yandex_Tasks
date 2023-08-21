def main():
    '''
    '''
    N, K = map(int, input().split())
    stones_dict = {}
    precious_stones = input()
    for stone in precious_stones:
        if stone not in stones_dict:
            stones_dict[stone] = 1
        else:
            stones_dict[stone] += 1
    
    beautiful_couples_dict = {}
    for _ in range(K):
        beautiful_couples = input()
        if beautiful_couples[0] not in beautiful_couples_dict:
            beautiful_couples_dict[beautiful_couples[0]] = []
        beautiful_couples_dict[beautiful_couples[0]].append(beautiful_couples[1])
    
    answer = 0
    for i in range(N-1):
        stones_dict[precious_stones[i]] -= 1
        if precious_stones[i] in beautiful_couples_dict:
            for stone in beautiful_couples_dict[precious_stones[i]]:
                answer += stones_dict[stone]
    
    print(answer)


    
if __name__ == '__main__':
	main()