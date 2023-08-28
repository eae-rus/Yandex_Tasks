def main():
    '''
    '''
    k = int(input())
    stroke = input()
    characters = set(stroke)
    
    max_beauty = 0
    for char in characters:
        left, right = 0, 0
        use_k = 0
        while left < len(stroke) and right < len(stroke):
            while right < len(stroke):
                if stroke[right] != char:
                    if use_k >= k:
                        break
                    use_k += 1
                right += 1
            max_beauty = max(max_beauty, right - left)
            if stroke[left] != char:
                use_k = max(use_k - 1, 0)
            left += 1
    
    print(max_beauty)
     
if __name__ == '__main__':
	main()