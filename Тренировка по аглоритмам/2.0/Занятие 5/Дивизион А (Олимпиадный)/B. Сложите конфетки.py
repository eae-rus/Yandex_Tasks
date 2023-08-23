def main():
    '''
    '''
    K = int(input())
    heaps_candy = []
    for _ in range(K):
        A, N = map(int, input().split())
        # сокращённый вариант, требуется проверить быстродейтсвие
        heaps_candy.extend([A] * N)
        # for _ in range(N):
        #     heaps_candy.append(A)
        
    left, right = 0, len(heaps_candy) - 1
    while right - left > 1:
        min_heaps = min(heaps_candy[left], heaps_candy[right])
        
        heaps_candy[left + 1] += min_heaps
        heaps_candy[right - 1] += min_heaps
        
        heaps_candy[left] -= min_heaps
        if heaps_candy[left] == 0:
            left += 1
        
        heaps_candy[right] -= min_heaps
        if heaps_candy[right] == 0:
            right -= 1
        
    print(right - left + 1)
    if right - left == 0:
        print(heaps_candy[left])
    else:
        print(heaps_candy[left], heaps_candy[right])

    
if __name__ == '__main__':
	main()