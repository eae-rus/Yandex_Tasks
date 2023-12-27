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
        heapq.heappush(heap, (0, start_node))
        result_dist = [ -1 for _ in range(N+1) ]
        result_dist[start_node] = 0
        visited_nodes = [ False for _ in range(N+1) ]
        while len(heap) > 0:
            dist, now_node = heapq.heappop(heap)
            if now_node == final_node:
                break
            visited_nodes[now_node] = True
            for dist_link, next_node in link_weights[now_node]: # dist_link, next_node
                dist_next_node = dist + dist_link
                if visited_nodes[next_node] == False and (result_dist[next_node] == -1 or dist_next_node < result_dist[next_node]):
                    heapq.heappush(heap, (dist_next_node, next_node))
                    result_dist[next_node] = dist_next_node
        return result_dist[final_node]
    
    N, K = map(int, input().split())
    link_weights = [ [] for _ in range(N+1) ]
    for i in range(K):
        a, b, weights = list(map(int, input().split()))
        link_weights[a].append((weights, b))
        link_weights[b].append((weights, a))
    start_node, final_node = map(int, input().split())
                
    dist = -1
    if start_node != final_node:
        dist = dijkstra(link_weights, start_node, final_node)
    else:
        dist = 0
    print(dist)
        
if __name__ == '__main__':
	main()