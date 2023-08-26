def main():
    '''
    '''
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    
    event = []
    for i in range(m):
        l,r = map(int, input().split())
        event.append((l, -1, i)) # начало
        event.append((r, 1, i)) # конец
    
    for cat in a:
        event.append((cat, 0, -1))
    
    event = sorted(event)
    count_line = [0] * m
    
    line_set = set()
    for event_i in event:
        if event_i[1] == -1: # начало
            line_set.add(event_i[2])
        
        if event_i[1] == 0: # кот
            for i in line_set:
                count_line[i] += 1
        
        if event_i[1] == 1: # конец
            line_set.remove(event_i[2])
    
    print(' '.join(map(str, count_line)))
    
if __name__ == '__main__':
	main()