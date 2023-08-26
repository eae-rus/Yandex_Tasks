def main():
    '''
    '''
    a,b,c,d = list(map(int, input().split()))
    
    left, right = -1002, 1002
    while right - left > 1e-6:
        mid = (left + right) / 2
        y = a * mid**3 + b * mid**2 + c * mid + d
        if y > 0:
            if a > 0:
                right = mid
            else:
                left = mid
        else:
            if a > 0:
                left = mid
            else:
                right = mid
    
    print((left + right) / 2)
    
if __name__ == '__main__':
	main()