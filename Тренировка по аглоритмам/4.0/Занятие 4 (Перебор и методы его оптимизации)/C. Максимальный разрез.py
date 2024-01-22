def calc_sum_edge(adjacency_edges, max_sum, node, cut_arr):
    '''
    '''
    for i in range(len(adjacency_edges)):
        if cut_arr[i] != cut_arr[node]+1:
            max_sum -= adjacency_edges[node][i]
        if cut_arr[i] != cut_arr[node]:
            max_sum += adjacency_edges[node][i]  
    
    return max_sum

def find_max_edge(adjacency_edges):
    '''
    '''
    cut_arr = [2] * len(adjacency_edges) # начинаю с 2, т.к. просят в условии задачи (идём в обратном порядке)
    previous_max_sum_dict = {}
    previous_max_sum_dict.update({tuple(cut_arr): 0})
    p_max_sum = 0

    cut_arr_answer = cut_arr.copy()
    max_sum_answer = 0
    
    while cut_arr[-1] == 2:
        node = 1
        
        is_end_add = False
        while not is_end_add:
            if cut_arr[node] - 1 <= 0:
                cut_arr[node] = 2
                node += 1
            else:
                p_max_sum = previous_max_sum_dict.get(tuple(cut_arr))
                cut_arr[node] -= 1
                is_end_add = True
        
        mow_sum = calc_sum_edge(adjacency_edges, p_max_sum, node,  cut_arr)
        previous_max_sum_dict.update({tuple(cut_arr): mow_sum})
        if mow_sum > max_sum_answer:
            max_sum_answer = mow_sum
            cut_arr_answer = cut_arr.copy()
   
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
    if cut_arr[1] == 1:
        for i in range(1, len(cut_arr)):
            if cut_arr[i] == 1:
                cut_arr[i] = 2
            else:
                cut_arr[i] = 1
    print(max_sum_edge)
    print(" ".join(map(str, cut_arr[1:])))
    

if __name__ == '__main__':
    main()