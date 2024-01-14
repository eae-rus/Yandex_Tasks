def calc_sum_edge(adjacency_edges, max_sum, node, cut_arr_old, cut_arr_new):
    '''
    '''
    for i in range(len(adjacency_edges)):
        if cut_arr_old[i] != cut_arr_old[node]:
            max_sum -= adjacency_edges[node][i]
    for i in range(len(adjacency_edges)):
        if cut_arr_new[i] != cut_arr_new[node]:
            max_sum += adjacency_edges[node][i]
    return max_sum

def find_max_edge(adjacency_edges, node = 1, max_sum = 0, cut_arr = []):
    '''
    '''
    if cut_arr == []:
        cut_arr = [2] * len(adjacency_edges) # начинаю с 2, т.к. просят в условии задачи
    if node >= len(adjacency_edges):
        return [max_sum, cut_arr]
    
    # 2 
    max_sum_answer = max_sum
    cut_arr_answer = cut_arr.copy
    
    new_max_sum, new_cut_arr = find_max_edge(adjacency_edges, node+1, max_sum, cut_arr.copy())
    if new_max_sum > max_sum_answer:
        max_sum_answer = new_max_sum
        cut_arr_answer = new_cut_arr.copy()
    
    # 1
    cut_arr_copy = cut_arr.copy()
    new_max_sum = max_sum
    if node != 1:
        cut_arr_copy[node] = 1 # замена (можно добавить 2,3,4 и т.д.)
        new_max_sum = calc_sum_edge(adjacency_edges, max_sum, node, cut_arr, cut_arr_copy)
        if new_max_sum > max_sum_answer:
            max_sum_answer = new_max_sum
            cut_arr_answer = cut_arr_copy.copy()
    
    new_max_sum, new_cut_arr = find_max_edge(adjacency_edges, node+1, new_max_sum, cut_arr_copy)
    if new_max_sum > max_sum_answer:
        max_sum_answer = new_max_sum
        cut_arr_answer = new_cut_arr.copy()
        
    return [max_sum_answer, cut_arr_answer]
    

def main():
    '''
    '''
    N = int(input())
    adjacency_edges = [[0] * (N+1)]
    for _ in range(N):
        adjacency_edges.append([0] + list(map(int, input().split())))

    # Вызываем функцию для подсчета количества разрезов
    max_sum_edge, cut_arr = find_max_edge(adjacency_edges)
    print(max_sum_edge)
    print(" ".join(map(str, cut_arr[1:])))
    

if __name__ == '__main__':
    main()