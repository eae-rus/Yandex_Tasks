def main():
    '''
    '''
    cutting_down_trees_1, rest_1, cutting_down_trees_2, rest_2, sum_trees = map(int, input().split())
    
    left = -3 + sum_trees // (cutting_down_trees_1 * (1-1/rest_1) + cutting_down_trees_2 * (1-1/rest_2))
    right = 3 + sum_trees // (cutting_down_trees_1 * (1-1/rest_1) + cutting_down_trees_2 * (1-1/rest_2))
    
    while left < right:
        mid = (left + right) // 2
        rest_1_days = mid // rest_1
        rest_2_days = mid // rest_2
        cutting_down_trees =  (mid - rest_1_days) * cutting_down_trees_1 + (mid - rest_2_days) * cutting_down_trees_2
        if cutting_down_trees >= sum_trees:
            right = mid
        else:
            left = mid + 1
    
    print(int(right))
    
if __name__ == '__main__':
	main()