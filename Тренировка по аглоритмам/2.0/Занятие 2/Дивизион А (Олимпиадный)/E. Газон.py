def main():
    '''
    '''
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3, y3, r = list(map(int, input().split()))
    
    # первое решение, сомневаюсь, что оно рационально, ибо большой перебор... Но попробуем в лоб
    lawn_bundles_count = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if (x-x3)**2 + (y-y3)**2 <= r**2:
                lawn_bundles_count += 1
    
    print(lawn_bundles_count)
    
if __name__ == '__main__':
	main()