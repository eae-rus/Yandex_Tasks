from math import ceil, floor

def main():
    '''
    '''
    x1, y1, x2, y2 = list(map(int, input().split()))
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    x3, y3, r = list(map(int, input().split()))
    
    # первое решение, сомневаюсь, что оно рационально, ибо большой перебор... Но попробуем в лоб
    lawn_bundles_count = 0
    for y in range(max(y1, y3-r), min(y2, y3+r)+1):
        x_delta = (r**2 - (y - y3)**2)**0.5
        x_max = min(x2, floor(x3 + x_delta))
        x_min = max(x1, ceil(x3 - x_delta))
        if x_max >= x_min:
            lawn_bundles_count += x_max - x_min + 1
    
    print(lawn_bundles_count)
    
if __name__ == '__main__':
	main()