def main():
    '''
    '''
    def find_min_k(x, line):
        count_line = 1
        max_right = x[0] + line
        for x_i in x[1:]:
            if x_i > max_right:
                count_line += 1
                max_right = x_i + line
        
        return count_line

    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    x = sorted(x)
    
    left = 0
    right = x[-1] - x[0]
    while left < right:
        line = (left + right) // 2
        count_line = find_min_k(x, line)
        if count_line < k:
            right = line - 1
        elif count_line == k:
            if find_min_k(x, line-1) == k:
                right = line - 1
            else:
                left = line
                right = line
        else:
            left = line

    print(right)
    
if __name__ == '__main__':
	main()