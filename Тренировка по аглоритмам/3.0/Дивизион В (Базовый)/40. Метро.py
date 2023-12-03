def main():
    N  = int(input())
    M  = int(input())
    visited_lines = [False for _ in range(M+1)]
    station_in_lines_matrix = [[False for _ in range(N+1)] for _ in range(M+1)]
    
    station_in_lines_arr = []
    station_in_lines_arr.append([])
    for line in range(1, M+1):
        station_i = list(map(int, input().split()))
        station_in_lines_arr.append(station_i[1:])
        for station in station_i[1:]:
            station_in_lines_matrix[line][station] = True

    start_st, end_st = list(map(int, input().split()))
    
    lines_in_station_arr = []
    lines_in_station_arr.append([])
    for st in range(1, N+1):
        lines_in_station_loc = []
        for line in range(1, M+1):
            if station_in_lines_matrix[line][st]:
                lines_in_station_loc.append(line)
        lines_in_station_arr.append(lines_in_station_loc)
        
    
    is_finished = False
    
    distance = -1
    
    next_lines_arr = lines_in_station_arr[start_st]
    for line in next_lines_arr:
        visited_lines[line] = True
    
    while not is_finished:
        now_lines_arr = next_lines_arr.copy()
        next_lines_arr = []
        
        for line in now_lines_arr:
            for st in station_in_lines_arr[line]:
                if st == end_st:
                    is_finished = True
                    break
                for next_line in lines_in_station_arr[st]:
                    if not visited_lines[next_line]:
                        next_lines_arr.append(next_line)
                        visited_lines[next_line] = True

            if is_finished:
                break
        
        distance += 1
        if len(next_lines_arr) == 0 and not is_finished:
            is_finished = True
            distance = -1
    
    print(distance)
            
if __name__ == '__main__':
	main()