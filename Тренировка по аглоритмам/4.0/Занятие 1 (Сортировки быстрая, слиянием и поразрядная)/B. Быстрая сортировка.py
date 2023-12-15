def main():
    '''
    '''
    def quick_sort(arr, left = -1, right = None):
        if right is None:
            right = len(arr)
        if right - left < 2:
            return True
        else:
            new_left = left # left выходит за исследуемые границы слева
            new_mid = left + 1 # mid равен первой исследуемой точке
            new_right = right # right выходит за исследуемые границы справа
            i_med = (left + right) // 2
            x = arr[i_med]
            arr[i_med], arr[left + 1] = arr[left + 1], arr[i_med]
            while new_right - new_mid > 1:
                i_now = new_mid + 1
                if arr[i_now] < x:
                    new_left += 1
                    new_mid = i_now
                    arr[new_left], arr[i_now] = arr[i_now], arr[new_left]
                elif arr[i_now] == x:
                    new_mid = i_now
                else:
                    new_right -= 1
                    arr[i_now], arr[new_right] = arr[new_right], arr[i_now]
                    
            quick_sort(arr, left, new_left+1)
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