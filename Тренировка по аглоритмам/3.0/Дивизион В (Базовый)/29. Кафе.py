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
    direction = [["None" for _ in range(N+1)] for _ in range(N+1)]
    calculate_cost[0][0] = 0
    for day in range(N):
        for variant in range(day+1):
            if calculate_cost[day][variant] == max_cost:
                continue
            
            cost_this_day = cost_arr[day]
            
            if cost_this_day > 100:
                new_day_cost = calculate_cost[day][variant] + cost_this_day
                if new_day_cost < calculate_cost[day+1][variant+1]:
                    calculate_cost[day+1][variant+1] = new_day_cost
                    direction[day+1][variant+1] = "variant+1"
            else:
                new_day_cost = calculate_cost[day][variant] + cost_this_day
                if new_day_cost < calculate_cost[day+1][variant]:
                    calculate_cost[day+1][variant] = new_day_cost
                    direction[day+1][variant] = "variant"
            
            if variant > 0:
                new_day_cost = calculate_cost[day][variant]
                if new_day_cost < calculate_cost[day+1][variant-1]:
                    calculate_cost[day+1][variant-1] = new_day_cost
                    direction[day+1][variant-1] = "variant-1"

    min_cost = max_cost
    remaining_coupons = 0
    for variant in range(N+1): # FIXME: можно написать в обратном порядке с прерыванием
        if calculate_cost[N][variant] <= min_cost:
            min_cost = calculate_cost[N][variant]
            remaining_coupons = variant

    used_coupons = 0
    days_use_coupons = []
    remaining_coupons_i = remaining_coupons
    for day in range(N, 0, -1):
        if direction[day][remaining_coupons_i] == "variant+1":
            remaining_coupons_i -= 1
        elif direction[day][remaining_coupons_i] == "variant":
            continue
        else: # direction[day][remaining_coupons_i] == "variant-1":
            used_coupons += 1
            days_use_coupons.append(day)
            remaining_coupons_i += 1


    print(min_cost)  
    print(remaining_coupons, used_coupons)
    days_use_coupons = days_use_coupons[::-1]
    for day in days_use_coupons:
        print(day)
    
        
if __name__ == '__main__':
	main()
