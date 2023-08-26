def main():
    '''
    '''
    def find_min_index(array, number):
        if array[0] > number:
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
        if array[len(array)-1] < number:
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
    
    K = int(input())
    request = list(map(int, input().split()))
    for number in request:
        l,r = 0, 0
        
        # небольшой костыль на предыдущем алгоритме
        left = find_min_index(array, number)
        if left == -1:
            if array[left + 1] == number:
                l = left + 1
            else:
                print(0,0)
                continue
        else:
            if array[left] == number:
                l = left
            elif left < len(array) - 1: # array[left] < number:
                if array[left + 1] == number:
                    l = left + 1
                else:
                    print(0,0)
                    continue
            else:
                print(0,0)
                continue
        
        right = find_max_index(array, number)
        if right == len(array):
            if array[right - 1] == number:
                r = right - 1
        else:
            if array[right] == number:
                r = right
            elif right > 0:
                if array[right - 1] == number:
                    r = right - 1
        
        print(l+1, r+1)
    
if __name__ == '__main__':
	main()