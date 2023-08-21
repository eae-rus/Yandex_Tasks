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
    
    beautiful_couples_set = set()
    for _ in range(K):
        beautiful_couples = input()
        beautiful_couples_set.add(beautiful_couples)
        
    beautiful_couples_dict = {}
    for beautiful_couples in beautiful_couples_set:
        if beautiful_couples[0] not in beautiful_couples_dict:
            beautiful_couples_dict[beautiful_couples[0]] = []
        beautiful_couples_dict[beautiful_couples[0]].append(beautiful_couples[1])
    
    answer = 0
    for i in range(N-1):
        left_stone = precious_stones[i]
        stones_dict[left_stone] -= 1
        if left_stone in beautiful_couples_dict:
            for right_stone in beautiful_couples_dict[left_stone]:
                if right_stone in stones_dict:
                    answer += stones_dict[right_stone]
    
    print(answer)


    
if __name__ == '__main__':
	main()