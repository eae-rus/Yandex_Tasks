def main():
    '''
    '''
    M = int(input())
    is_add = True
    events = []
    while is_add:
        l,r = map(int, input().split())
        if l == 0 and r == 0:
            is_add = False
            continue
        
        if r <= 0 or l >= M:
            continue
        
        events.append((l,r))
        
    events = sorted(events)
    
    new_array = []
    max_right = 0
    now_best = (0,0)
        
    for event in events:
        if event[0] > max_right:
            new_array.append(now_best)
            max_right = now_best[1]
            if max_right >= M:
                break
        if event[0] <= max_right and event[1] > now_best[1]:
            now_best = event

    if max_right < M:
        new_array.append(now_best)


    if max_right < M:
        print('No solution')
    else:
        print(len(new_array))
        new_array.sort()
        for line in new_array:
            print(line[0], line[1])
    
if __name__ == '__main__':
	main()