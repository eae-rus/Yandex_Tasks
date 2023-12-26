import heapq

def main():
    '''
    '''
    def dijkstra(link_weights, start_node, final_node):
        '''
        '''
        N = len(link_weights)
        result_dist = -1
        # Создание пустой кучи
        heap = []
        for link in link_weights[start_node]:
            heapq.heappush(heap, link)
        result_dist = [ (-1, -1) for _ in range(N+1) ] # (-1, -1) - расстояние, предыдущий узел
        result_dist[start_node] = (0, start_node)
        while len(heap) > 0: # можно добавить прерывание по факту что "все маршруты больше пути до конечной точки"
            dist_link, now_node, next_node = heapq.heappop(heap)
            if result_dist[next_node][0] == -1 or result_dist[now_node][0] + dist_link < result_dist[next_node][0]:
                result_dist[next_node] = (result_dist[now_node][0] + dist_link, now_node)
                for link in link_weights[next_node]:
                    heapq.heappush(heap, link)
                    
        if result_dist[final_node] == (-1, -1):
            return -1
        else:
            route = []
            now_node = final_node
            while True:
                route.append(now_node)
                if now_node == start_node:
                    break
                now_node = result_dist[now_node][1]
            return route[::-1]
    
    N, start_node, final_node = map(int, input().split())
    link_weights = [ [] for _ in range(N+1) ]
    for i in range(N):
        weights = list(map(int, input().split()))
        for k in range(N):
            if weights[k] >= 0 and k != i:
                link_weights[i+1].append((weights[k], i+1, k+1)) # вес, начальный узел, конечный узел
                
    dist = -1
    if start_node != final_node:
        route = dijkstra(link_weights, start_node, final_node)
        if route != -1:
            print(' '.join(map(str, route)))
        else:
            print(-1)
    else:
        print(start_node)
        
if __name__ == '__main__':
	main()