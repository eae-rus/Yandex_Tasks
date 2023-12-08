def main():
    '''
    '''
    k = int(input())
    n = int(input())
    
    person_in_floor = [0 for _ in range(n)]
    for i in range(n):
        person_in_floor[i] = int(input())

    # FIXME: нужно исправить этот код
    last_floor = n
    sum_time = last_floor
    people_in_elevator = 0
    while last_floor > 0:
        person_floor = person_in_floor[last_floor - 1] + people_in_elevator
        if (person_floor) < k:
            people_in_elevator = person_floor
            sum_time += 1
            last_floor -= 1
            continue
        
        remainder_person = person_floor % k
        if remainder_person % k != 0:
            sum_time += person_floor // k * (2 * last_floor) + 1
            last_floor -= 1
            people_in_elevator = remainder_person
        else:
            people_in_elevator = 0
            sum_time += person_floor // k * (2 * last_floor) - 1
            last_floor -= 1

    print(sum_time)
        
if __name__ == '__main__':
	main()