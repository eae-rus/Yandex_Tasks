def calc_sum_edge(adjacency_edges, max_sum, node, cut_arr):
    '''
    '''
    for i in range(len(adjacency_edges)):
        if cut_arr[i] != cut_arr[node]:
            max_sum -= adjacency_edges[node][i]
    cut_arr[node] = 1
    for i in range(len(adjacency_edges)):
        if cut_arr[i] != cut_arr[node]:
            max_sum += adjacency_edges[node][i]  

    return max_sum

def find_max_edge(adjacency_edges, node, max_sum, cut_arr):
    '''
    '''
    if node > len(adjacency_edges):
        return [max_sum, cut_arr]

    max_sum_answer = max_sum
    mow_sum = 0
    cut_arr_answer = cut_arr.copy()
    if node != 1:
        mow_sum = calc_sum_edge(adjacency_edges, max_sum, node,  cut_arr)
        if mow_sum > max_sum_answer:
            max_sum_answer = mow_sum
            cut_arr_answer = cut_arr.copy()

    node += 1
    while node < len(adjacency_edges):
        new_max_sum, new_cut_arr = find_max_edge(adjacency_edges, node, mow_sum, cut_arr.copy())
        if new_max_sum > max_sum_answer:
            max_sum_answer = new_max_sum
            cut_arr_answer = new_cut_arr.copy()
        node += 1
        
    return [max_sum_answer, cut_arr_answer]
    

def main():
    '''
    '''
    N = int(input())
    adjacency_edges = [[0] * (N+1)]
    for _ in range(N):
        adjacency_edges.append([0] + list(map(int, input().split())))

    # Вызываем функцию для подсчета количества разрезов
    cut_arr = [2] * len(adjacency_edges) # начинаю с 2, т.к. просят в условии задачи
    max_sum_edge, cut_arr = find_max_edge(adjacency_edges, 1, 0, cut_arr)
    print(max_sum_edge)
    print(" ".join(map(str, cut_arr[1:])))
    

if __name__ == '__main__':
    main()