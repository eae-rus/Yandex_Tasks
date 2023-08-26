def main():
    '''
    '''
    N = int(input())
    event = []
    for _ in range(N):
        start, time = map(int, input().split())
        # 1 - начало, -1 - конец
        event.append((start, 1))
        event.append((start + time, -1))
    
    event = sorted(event)
    count = 0
    max_count = 0
    for event_i in event:
        if event_i[1] == 1: # начало
            count += 1
        else: # event_i[1] == -1 (конец)
            count -= 1
        
        if max_count < count:
            max_count = count
    
    print(max_count)
    
if __name__ == '__main__':
	main()