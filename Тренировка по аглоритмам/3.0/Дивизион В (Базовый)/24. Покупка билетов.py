def main():
    N = int(input())

    one_ticket, two_ticket, three_ticket = [0] * (N+2), [0] * (N+2), [0] * (N+2)
    one_ticket[0], two_ticket[0], three_ticket[0] = 0, 3600*4, 3600*4
    one_ticket[1], two_ticket[1], three_ticket[1] = 0, 3600*4, 3600*4
    for i in range(2, N+2):
        one_ticket[i], two_ticket[i], three_ticket[i] = map(int, input().split())
        
    min_time = [0, 0, 0] # i = 0 (перед тобой на 1 шаг), 1 (перед тобой на 2 шага), 2 (перед тобой на 3 шага)
    for i in range(2, N+2):
        variant_1 = one_ticket[i] + min_time[0]
        variant_2 = two_ticket[i-1] + min_time[1]
        variant_3 = three_ticket[i-2] + min_time[2]
        min_time[0], min_time[1], min_time[2] = min(variant_1, variant_2, variant_3), min_time[0], min_time[1]
        
    print(min_time[0])
    
        
if __name__ == '__main__':
	main()
