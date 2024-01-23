def find_len_min_cycle(adjacency_edges, is_visited, node, sum_edge):
    '''
    '''
    is_visited[node] = True
    
    if all(is_visited):
        is_visited[node] = False
        if adjacency_edges[node][1] == 0:
            return -1
        return sum_edge + adjacency_edges[node][1]
    
    answer = -1
    for i in range(2, len(adjacency_edges)):
        if not is_visited[i] and adjacency_edges[node][i] != 0:
            sum_edge_i = sum_edge + adjacency_edges[node][i]
            answer_i = find_len_min_cycle(adjacency_edges, is_visited, i, sum_edge_i)
            if answer == -1:
                answer = answer_i
            elif answer_i != -1:
                answer = min(answer, answer_i)

    is_visited[node] = False
    return answer

def main():
    '''
    '''
    N = int(input())
    adjacency_edges = [[0] * (N+1)]
    for _ in range(N):
        adjacency_edges.append([0] + list(map(int, input().split())))
    
    is_visited = [False] * (N+1)
    is_visited[0] = True
    node, sum_edge = 1, 0
    answer = 0
    if N > 1:
        answer = find_len_min_cycle(adjacency_edges, is_visited, node, sum_edge)
    print(answer)
    
if __name__ == '__main__':
    main()