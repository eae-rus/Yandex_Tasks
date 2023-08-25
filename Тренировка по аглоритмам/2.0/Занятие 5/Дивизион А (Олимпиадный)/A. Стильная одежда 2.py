def main():
    '''
    '''
    N = int(input())
    cap_color_arr = map(int, input().split())
    cap_color_arr = sorted(cap_color_arr)
    min_cap_color = cap_color_arr[0]
    max_cap_color = cap_color_arr[-1]
    
    N = int(input())
    t_shirt_color_arr = map(int, input().split())
    t_shirt_color_arr = sorted(t_shirt_color_arr)
    min_t_shirt_color = t_shirt_color_arr[0]
    max_t_shirt_color = t_shirt_color_arr[-1]
    
    N = int(input())
    pants_color_arr = map(int, input().split())
    pants_color_arr = sorted(pants_color_arr)
    min_pants_color = pants_color_arr[0]
    max_pants_color = pants_color_arr[-1]
    
    N = int(input())
    shoe_color_arr = map(int, input().split())
    shoe_color_arr = sorted(shoe_color_arr)
    min_shoe_color = shoe_color_arr[0]
    max_shoe_color = shoe_color_arr[-1]
    
    

    
if __name__ == '__main__':
	main()