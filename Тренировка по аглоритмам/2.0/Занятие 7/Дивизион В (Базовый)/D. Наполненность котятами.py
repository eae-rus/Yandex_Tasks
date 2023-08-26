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
    count_line = [[0,0] for _ in range(n)]
    сount_cat = 0
    for event_i in event:
        if event_i[1] == -1: # начало
            count_line[event_i[2]][0] = сount_cat
        elif event_i[1] == 0: # кот
            сount_cat += 1        
        elif event_i[1] == 1: # конец
            count_line[event_i[2]][1] = сount_cat
    
    for i in range(m):
        count_line[i] = count_line[i][1] - count_line[i][0]
        
    print(' '.join(map(str, count_line)))
    
if __name__ == '__main__':
	main()