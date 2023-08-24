def main():
    '''
    '''
    n = int(input())
    a = list(map(int, input().split()))
    
    a_prefix_sum = [0] * (n+1)
    max_sum = a[0]
    for i in range(n):
        if a[i] >= 0:
            a_prefix_sum[i+1] = a_prefix_sum[i] + a[i]
            if a_prefix_sum[i+1] > max_sum:
                max_sum = a_prefix_sum[i+1]
        else:
            a_prefix_sum[i+1] = 0
            if a[i] > max_sum:
               max_sum = a[i]
      
    print(max_sum)

if __name__ == '__main__':
	main()