def main():
    N = int(input())
    
    cost_arr = [0]*N
    for day in range(N):
        cost_arr[day] = int(input())
        
    # защиты
    if N == 0:
        print(0)
        print("0 0")
        return
    if N == 1:
        print(1)
        if cost_arr[0] > 100:
            print("1 0")
        else:
            print("0 0")
        return
    
    max_cost = 300*101+1
    calculate_cost = [[max_cost for _ in range(N+1)] for _ in range(N+1)]
    calculate_cost[0][0] = 0
    for day in range(N):
        for variant in range(day+1):
            if calculate_cost[day][variant] == max_cost:
                continue
            
            cost_this_day = cost_arr[day]
            
            if cost_this_day > 100:
                new_day_cost = calculate_cost[day][variant] + cost_this_day
                calculate_cost[day+1][variant+1] = min(calculate_cost[day+1][variant+1], new_day_cost)
            else:
                new_day_cost = calculate_cost[day][variant] + cost_this_day
                calculate_cost[day+1][variant] = min(calculate_cost[day+1][variant], new_day_cost)
            
            if variant > 0:
                new_day_cost = calculate_cost[day][variant]
                calculate_cost[day+1][variant-1] = min(calculate_cost[day+1][variant-1], new_day_cost)
     
    min_cost = max_cost
    for variant in range(N+1):
        min_cost = min(min_cost, calculate_cost[N][variant])
    
    print(min_cost)  
    
        
if __name__ == '__main__':
	main()
