def main():
    '''
    '''
    def quick_sort(arr, left = -1, right = None):
        # FIXME: пока что не работает, я не правильно двигаю границы
        if right is None:
            right = len(arr)
        if right - left < 2:
            return True
        else:
            new_left = left
            new_right = right
            x = arr[new_left + 1]
            new_left += 1
            while new_right - new_left > 1:
                if arr[new_left + 1] <= x:
                    new_left += 1
                    arr[new_left - 1], arr[new_left] = arr[new_left], arr[new_left - 1]
                else:
                    new_right -= 1
                    arr[new_left + 1], arr[new_right] = arr[new_right], arr[new_left + 1]
                    
            quick_sort(arr, left, new_left)
            quick_sort(arr, new_right-1, right)
            return True
    
    N = int(input())
    arr = list(map(int, input().split()))
    left = -1
    right = len(arr)
    
    quick_sort(arr, left, right)
    
    print(" ".join(map(str, arr)))
            
if __name__ == '__main__':
	main()