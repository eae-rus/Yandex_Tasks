import math

def main():
    '''
    '''
    N = int(input())
    r1_max, r2_min = 0, (1 + 10**6)
    
    events = []
    for _ in range(N):
        r1, r2, angle_1, angle_2 = map(float, input().split())
        
        if r1 > r1_max:
            r1_max = r1
        if r2 < r2_min:
            r2_min = r2
            
        if angle_2 >= angle_1:
            events.append((angle_1, 1)) # 1 - начало
            events.append((angle_2, -1)) # -1 - конец
        else:
            events.append((0, 1)) # 1 - начало
            events.append((angle_2, -1)) # -1 - конец
            #------
            events.append((angle_1, 1)) # 1 - начало
            events.append((2*math.pi, -1)) # -1 - конец
    
    if r1_max > r2_min:
        print(0)
        return
    
    events = sorted(events)
    zone = []
    count = 0
    for angle, event_type in events:
        if event_type == -1: # конец
            if count == N:
                zone.append((angle, -1))
            count -= 1
        else: # event_type == 1 (начало)
            count += 1
            if count == N:
                zone.append((angle, 1))
                
    if len(zone) == 0:
        print(0)
        return
    
    sum_square = 0
    for i in range(0, len(zone), 2):
        anngle_start, angle_end = zone[i][0], zone[i+1][0]
        square_1 = r1_max**2 * (angle_end - anngle_start) / 2# / math.pi
        square_2 = r2_min**2 * (angle_end - anngle_start) / 2# / math.pi
        sum_square += square_2 - square_1
    print(sum_square)
    
if __name__ == '__main__':
	main()