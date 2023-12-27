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
        result_dist = [ -1 for _ in range(N+1) ]
        result_dist[start_node] = 0
        while len(heap) > 0: # можно добавить прерывание по факту что "все маршруты больше пути до конечной точки"
            dist_link, now_node, next_node = heapq.heappop(heap)
            if result_dist[next_node] == -1 or result_dist[now_node] + dist_link < result_dist[next_node]:
                result_dist[next_node] = result_dist[now_node] + dist_link
                for link in link_weights[next_node]:
                    heapq.heappush(heap, link)
        return result_dist[final_node]
    
    N, K = map(int, input().split())
    link_weights = [ [] for _ in range(N+1) ]
    for i in range(K):
        a, b, weights = list(map(int, input().split()))
        link_weights[a].append((weights, a, b))
        link_weights[b].append((weights, b, a))
    start_node, final_node = map(int, input().split())
                
    dist = -1
    if start_node != final_node:
        dist = dijkstra(link_weights, start_node, final_node)
    else:
        dist = 0
    print(dist)
        
if __name__ == '__main__':
	main()