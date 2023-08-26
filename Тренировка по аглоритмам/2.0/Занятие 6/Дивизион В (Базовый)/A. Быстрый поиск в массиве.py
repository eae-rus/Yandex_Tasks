def main():
    '''
    '''
    def find_min_index(array, number):
        if array[0] >= number:
            return -1
        
        left, right = 0, len(array)-1
        while left < right - 1:
            mid = (left + right) // 2
            if array[mid] >= number:
                right = mid
            else:
                left = mid
        
        if array[right] < number:
            return right
        elif array[left] >= number:
            return left - 1
        else:
            return left
    
    def find_max_index(array, number):
        if array[len(array)-1] <= number:
            return len(array)
        
        left, right = 0, len(array)-1
        while left < right:
            mid = (left + right) // 2
            if array[mid] <= number:
                left = mid + 1
            else:
                right = mid
                
        if array[right] > number:
            return right
        elif array[left] == number:
            return right + 1
        else:
            return right
    
    N = int(input())
    array = list(map(int, input().split()))
    array = sorted(array)
    
    K = int(input())
    answer = []
    for _ in range(K):
        L, R = map(int, input().split())
        count = find_max_index(array, R) - find_min_index(array, L) - 1
        if count > 0:
            answer.append(count)
        else:
            answer.append(0)
    
    print(' '.join(map(str, answer)))
    
if __name__ == '__main__':
	main()