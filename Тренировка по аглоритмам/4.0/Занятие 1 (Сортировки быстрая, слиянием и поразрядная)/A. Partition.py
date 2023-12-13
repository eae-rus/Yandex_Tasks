def main():
    '''
    '''
    N = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    left_part = -1
    right_part = len(arr)
    while left_part + 1 < right_part:
        if arr[left_part + 1] < x:
            left_part += 1
        else:
            right_part -= 1
            arr[left_part + 1], arr[right_part] = arr[right_part], arr[left_part + 1]
            
    print(left_part + 1)
    print(len(arr) - right_part)
            
if __name__ == '__main__':
	main()