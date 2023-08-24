def main():
    '''
    '''
    n,q = map(int, input().split())
    a_prefix_sum = list(map(int, input().split()))
    
    for i in range(1, n):
        a_prefix_sum[i] = a_prefix_sum[i] + a_prefix_sum[i-1]

    for _ in range(q):
        l,r = map(int, input().split())
        if l == 1:
            print(a_prefix_sum[r-1])
        else:
            print(a_prefix_sum[r-1] - a_prefix_sum[l-2])
    

    
if __name__ == '__main__':
	main()