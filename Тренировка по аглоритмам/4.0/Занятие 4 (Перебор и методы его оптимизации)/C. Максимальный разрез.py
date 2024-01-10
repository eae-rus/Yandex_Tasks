def is_all_visited(visited):
    '''
    '''
    for i in visited:
        if not i:
            return False
    return True

def find_max_edge(node, adjacency_edges, visited):
    new_node = 0
    max_edge = 0
    for i in range(1, len(adjacency_edges)):
        if adjacency_edges[node][i] > max_edge and not visited[i]:
            max_edge = adjacency_edges[node][i]
            new_node = i
    return [new_node, max_edge]

def count_cut_pieces(adjacency_edges):
    '''
    '''
    N = len(adjacency_edges)
    
    max_sum_edge = 0
    node = 1
    visited = [False] * (N)
    visited[0] = True
    cut_arr = [0] * (N)
    cut = 1
    while not is_all_visited(visited):
        visited[node] = True
        cut_arr[node] = cut + 1
        cut = (cut + 1) % 2 # Переключаем цвет, реализован простейший алгоритм
        new_node, edge = find_max_edge(node, adjacency_edges, visited)
        max_sum_edge += edge
        
        if new_node != 0:
            node = new_node
        elif cut_arr[1] != cut_arr[node]:
            max_sum_edge += adjacency_edges[1][node]
        
    max_sum = 0
    for i in range(1, N):
        for j in range(i+1, N):
            if cut_arr[i] != cut_arr[j]:
                max_sum += adjacency_edges[i][j]
        
    return max_sum, cut_arr

def main():
    '''
    '''
    N = int(input())
    adjacency_edges = [[0] * (N+1)]
    for _ in range(N):
        adjacency_edges.append([0] + list(map(int, input().split())))

    # Вызываем функцию для подсчета количества разрезов
    max_sum_edge, cut_arr = count_cut_pieces(adjacency_edges)
    print(max_sum_edge)
    print(" ".join(map(str, cut_arr[1:])))
    

if __name__ == '__main__':
    main()