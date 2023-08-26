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
        
        events.append((l,-1,(l,r)))
        events.append((r,1,(l,r)))
        
    events = sorted(events)
    
    new_array = []
    line_dict = {}
    count_line = 0
    is_no_solution = False
    for event in events:
        if event[1] == -1:
            if event[2] not in line_dict:
                line_dict[event[2]] = 0
            line_dict[event[2]] += 1
            count_line += 1
        else:
            line_dict[event[2]] -= 1
            if line_dict[event[2]] == 0:
                del line_dict[event[2]]
            count_line -= 1
            if count_line == 0 and event[0] < M:
                is_no_solution = True
                break
            
            unique = True 
            for key in line_dict:
                l,r = key
                if event[2][0] > l and event[2][1] < r:
                    unique = False
                    break
            
            if unique:
                new_array.append(event[2])

    if is_no_solution or len(new_array) == 0:
        print('No solution')
    else:
        print(len(new_array))
        new_array.sort()
        for line in new_array:
            print(line[0], line[1])
    
if __name__ == '__main__':
	main()