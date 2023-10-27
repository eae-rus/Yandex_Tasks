def main():
    N, M = list(map(int, input().split()))
    
    graph = {i: [] for i in range(1, N+1)}
    visited_count = {i: 0 for i in range(1, N+1)}
    for _ in range(M):
        node_1, node_2 = list(map(int, input().split()))
        if node_1 != node_2:
            graph[node_1].append(node_2)
            visited_count[node_2] += 1
        
    is_cycle_found = False
    topologized_graph = []
    while len(graph) > 0 and not is_cycle_found:
        is_cycle_found = True
        keys = list(graph.keys())
        for key in keys:
            if visited_count[key] == 0:
                is_cycle_found = False
                for next_node in graph[key]:
                    visited_count[next_node] -= 1
                topologized_graph.append(key)
                del graph[key]
    
    if is_cycle_found:
        print("-1")
    else:
        print(" ".join(map(str, topologized_graph)))

        
if __name__ == '__main__':
	main()
