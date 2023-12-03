import math

def main():
    def calc_distance(x1, y1, x2, y2):
        R1 = math.sqrt(x1**2 + y1**2)
        R2 = math.sqrt(x2**2 + y2**2)
        del_R = abs(R1 - R2)
        R_min = min(R1, R2)

        del_angle = math.atan2(y2, x2) - math.atan2(y1, x1)
        if del_angle > math.pi:
            del_angle -= 2 * math.pi
        elif del_angle < -math.pi:
            del_angle += 2 * math.pi
        
        distance_R_angle = del_R + R_min * abs(del_angle)
        distance_R_to_R = R1 + R2
        distance = min(distance_R_angle, distance_R_to_R)
        return distance
    
    x1, y1, x2, y2  = list(map(int, input().split()))

    distance = calc_distance(x1, y1, x2, y2)

    print(distance)
        
if __name__ == '__main__':
	main()