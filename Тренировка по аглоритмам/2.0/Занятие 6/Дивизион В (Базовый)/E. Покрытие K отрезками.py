def main():
    '''
    '''
    def find_min_k(x, line):
        count_line = 1
        left = x[0]
        for x_i in x[1:]:
            if x_i - left > line:
                count_line += 1
                left = x_i
        
        return count_line

    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    x = sorted(x)
    
    left = 0
    right = x[-1] - x[0]
    while left < right - 1:
        mid = (left + right) // 2
        if find_min_k(x, mid) > k:
            left = mid
        else:
            right = mid

    if find_min_k(x, left) == k:
        print(left)
    else:
        print(right)
    
if __name__ == '__main__':
	main()