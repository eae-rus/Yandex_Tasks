def main():
    '''
    '''
    K = int(input())
    x, y = map(int, input().split())
    x_min, x_max = x, x
    y_min, y_max = y, y
    for _ in range(K-1):
        x, y = map(int, input().split())
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
    
    answer = [x_min, y_min, x_max, y_max]
    print(' '.join(map(str, answer)))
     
if __name__ == '__main__':
	main()