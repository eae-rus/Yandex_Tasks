import heapq

def main():
    '''
    '''
    def dijkstra(link_travel, start_node, final_node):
        '''
        '''
        N = len(link_travel)
          # Создание пустой кучи
        heap = []
        heapq.heappush(heap, (0, start_node))
        result_dist = [ -1 for _ in range(N+1) ]
        result_dist[start_node] = 0
        visited_nodes = [ False for _ in range(N+1) ]
        while len(heap) > 0:
            t_now, now_node = heapq.heappop(heap)
            if now_node == final_node:
                break
            visited_nodes[now_node] = True
            for t_start, t_arrival, next_node in link_travel[now_node]: #t_start, t_arrival, b
                t_next_node = t_arrival
                if (visited_nodes[next_node] == False and t_now <= t_start and
                    (result_dist[next_node] == -1 or t_next_node < result_dist[next_node])):
                    heapq.heappush(heap, (t_next_node, next_node))
                    result_dist[next_node] = t_next_node
        return result_dist[final_node]
    
    N = int(input())
    start_node, final_node = map(int, input().split())    
    link_travel = [ [] for _ in range(N+1) ]
    R = int(input())
    for _ in range(R):
        a, t_start, b, t_arrival = list(map(int, input().split()))
        link_travel[a].append((t_start, t_arrival, b))
                
    dist = -1
    if start_node != final_node:
        dist = dijkstra(link_travel, start_node, final_node)
    else:
        dist = 0
    print(dist)
        
if __name__ == '__main__':
	main()