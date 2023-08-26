def main():
    '''
    '''
    N = int(input())
    event = []
    for _ in range(N):
        start, end = map(int, input().split())
        # -1 - начало, 1 - конец
        event.append((start, -1))
        event.append((end, 1))
    
    event = sorted(event)
    shaded_length = 0
    count_line = 0
    previous_event_coordinate = event[0][0]
    for event_i in event:
        if count_line > 0:
            shaded_length += event_i[0] - previous_event_coordinate
        previous_event_coordinate = event_i[0]

        if event_i[1] == -1: # начало
            count_line += 1
        else: # event_i[1] == 1 (конец)
            count_line -= 1
    
    print(shaded_length)
    
if __name__ == '__main__':
	main()