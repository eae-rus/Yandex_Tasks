def main():
    '''
    '''
    N = int(input())
    Layland_sity_cost = list(map(int, input().split()))
    
    new_Layland_sity = [-1]*N
    stack_sity = []
    for i in range(N):
        while stack_sity and Layland_sity_cost[i] < stack_sity[-1][1]:
            number, cost = stack_sity.pop()
            new_Layland_sity[number] = i
        stack_sity.append((i, Layland_sity_cost[i]))

    print(" ".join(map(str, new_Layland_sity)))
    
        
if __name__ == '__main__':
	main()