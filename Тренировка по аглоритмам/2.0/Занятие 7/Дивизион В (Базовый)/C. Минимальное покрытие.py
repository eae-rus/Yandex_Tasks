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
    is_no_solution = False
    max_right = 0
    max_right_line = events[0]
    for event in events:
        if event[0] <= max_right:
            if event[1] > max_right_line[1]:
                max_right_line = event
        else:
            if event[0] > max_right_line[1]:
                is_no_solution = True
                break
            else:
                max_right = max_right_line[1]
                new_array.append(max_right_line)
                max_right_line = event

    new_array.append(max_right_line)

    if is_no_solution or len(new_array) == 0:
        print('No solution')
    else:
        print(len(new_array))
        new_array.sort()
        for line in new_array:
            print(line[0], line[1])
    
if __name__ == '__main__':
	main()