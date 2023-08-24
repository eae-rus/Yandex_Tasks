def main():
    '''
    '''
    n = int(input())
    a_prefix_sum = list(map(int, input().split()))
    
    max_sum = a_prefix_sum[0]
    for i in range(1, n):
        a_prefix_sum[i] = a_prefix_sum[i-1] + a_prefix_sum[i]
        if a_prefix_sum[i] > max_sum:
            max_sum = a_prefix_sum[i]

    print(max_sum)

if __name__ == '__main__':
	main()