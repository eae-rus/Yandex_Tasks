def main():
    '''
    '''
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    
    a_prefix_sum = [0] * (n+1)
    for i in range(n):
        a_prefix_sum[i+1] = a_prefix_sum[i] + a[i]

    for _ in range(q):
        l,r = map(int, input().split())
        print(a_prefix_sum[r] - a_prefix_sum[l-1])
    

    
if __name__ == '__main__':
	main()