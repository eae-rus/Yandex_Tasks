import heapq

def main():
    '''
    '''
    N = int(input())
    T_V = [[0, 0] for _ in range(N+1)] # T - время посадки, V - скорость движения
    for i in range(1, N+1):
        T_V[i][0], T_V[i][1] = map(int, input().split())
    
    roads = [[] for _ in range(N+1)]
    for _ in range(N-1):
        A, B, S = map(int, input().split())
        roads[A].append([A, B, S])
        roads[B].append([B, A, S])

    # Считаем расстояния до всех городов от столицы
    # Так как это дерево, то маршрут только 1.
    dist = [[-1] * (N+1) for _ in range(N+1)] # Матрица всех расстояний
    for i in range(1, N+1):
        visited = [False] * (N+1)
        dist[i][i], visited[i] = 0, True
        neighboring_cities = roads[i].copy()
        while neighboring_cities:
            city_now, city_next, dist_city = neighboring_cities.pop()
            if visited[city_next] == False:
                dist[i][city_next] = dist[i][city_now] + dist_city
                visited[city_next] = True
                for A, B, S in roads[city_next]:
                    neighboring_cities.append([A, B, S])

    # Считаем кратчайшие время до всех городов
    visited = [False] * (N+1)
    visited[1] = True
    heap = []
    for city in range(2, N+1): # первичная загрузка в кучу
        time = dist[1][city] / T_V[city][1] + T_V[city][0]
        heapq.heappush(heap, [time, city, [1]])

    last_Olympic_Athletes = [0, [1]]
    while heap:
        time, city_now, road = heapq.heappop(heap)
        road.append(city_now)
        last_Olympic_Athletes = [time, city_now, road]
        for i in range(len(heap)):
            time_next, city_next, road_next = heap[i]
            dist_A_B = dist[city_now][city_next]
            new_time = time + dist_A_B / T_V[city_next][1] + T_V[city_next][0]
            if new_time - time_next < 0:
                road_next = road.copy()
                heap[i] = [new_time, city_next, road_next]

    time, city_now, road = last_Olympic_Athletes
    road = road[::-1]
    print(time)
    print(" ".join(map(str, road)))
        
if __name__ == '__main__':
	main()