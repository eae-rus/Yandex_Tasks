def main():
    '''
    '''
    def find_count(stickers, min_sticker):
        if stickers[-1] < min_sticker:
            return len(stickers)
        if stickers[0] >= min_sticker:
            return 0
        
        left, right = 0, len(stickers) - 1
        while left < right-1:
            mid = (left + right) // 2
            if stickers[mid] >= min_sticker:
                right = mid-1
            else:
                left = mid
        
        if stickers[right] < min_sticker:
            return right + 1
        return left + 1
    
    N = int(input())
    diego_stickers = set(map(int, input().split()))
    diego_stickers = list(diego_stickers)
    diego_stickers.sort()
    
    K = int(input())
    collectors_stickers = map(int, input().split())
    for min_sticker in collectors_stickers:
        count_stickers = find_count(diego_stickers, min_sticker)
        print(count_stickers)
    

     
if __name__ == '__main__':
	main()