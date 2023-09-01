def main():
    '''
    '''
    A_hh, A_mm, A_ss = map(int, input().split(":"))
    A_time = A_hh * 3600 + A_mm * 60 + A_ss
    B_hh, B_mm, B_ss = map(int, input().split(":"))
    B_time = B_hh * 3600 + B_mm * 60 + B_ss
    C_hh, C_mm, C_ss = map(int, input().split(":"))
    C_time = C_hh * 3600 + C_mm * 60 + C_ss
    
    if A_time > C_time:
        C_time += 24 * 3600
        
    diff_2 = (C_time - A_time) / 2
    
    coorect_time = B_time + diff_2
    if coorect_time >= 24 * 3600:
        coorect_time -= 24 * 3600
        
    coorect_time_hh = int(coorect_time // 3600)
    coorect_time -= coorect_time_hh * 3600
    
    coorect_time_mm = int(coorect_time // 60)
    coorect_time -= coorect_time_mm * 60
    
    coorect_time_ss = int(coorect_time // 1)
    coorect_time -= coorect_time_ss
    if coorect_time >= 0.5:
        coorect_time_ss += 1
    
    answer = []
    for time in [coorect_time_hh, coorect_time_mm, coorect_time_ss]:
        if time < 10:
            answer.append('0' + str(time))
        else:
            answer.append(str(time))
    
    print(':'.join(map(str, answer)))   
    
     
if __name__ == '__main__':
	main()