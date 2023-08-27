import sys

def main():
    '''
    '''
    def find_first_parant(not_found_set):
        not_found_list = list(not_found_set)
        for i in range(len(not_found_list)):
            is_parent = True
            for k in range(len(not_found_list)):
                if not_found_list[i][1] == not_found_list[k][0]:
                    is_parent = False
                    break
            if is_parent:
                return not_found_list[i]
    
    def add_descendant(tree, parent, descendant):
        if parent == tree[0]:
            descendant_tree = [descendant, []]
            tree[1].append(descendant_tree)
            return True
        else:
            for child in tree[1]:
                if add_descendant(child, parent, descendant):
                    return True
            return False
    
    def find_parant(tree, parent):
        if parent == tree[0]:
            return tree
        else:
            for child in tree[1]:
                new_tree = find_parant(child, parent)
                if new_tree is not None:
                    return new_tree
            return None
           
    def find_descendant(tree, descendant):
        if descendant == tree[0]:
            return True
        else:
            for child in tree[1]:
                if find_descendant(child, descendant):
                    return True
            return False
    
    N = int(input())
    not_found_set = set()
    for i in range(N-1):
        descendant, parent = input().split()
        not_found_set.add((descendant, parent))

    descendant, parent = find_first_parant(not_found_set)
    descendant_tree = [descendant, []]
    tree = [parent, [descendant_tree]]
    not_found_set.remove((descendant, parent))
    
    i = 0
    while i < 1000 and not_found_set:
        i += 1
        for descendant, parent in list(not_found_set):
            if add_descendant(tree, parent, descendant):
                not_found_set.remove((descendant, parent))
    
    answer = []
    query = sys.stdin.readline()[0:-1].split(" ")
    while not (query == ""):
        try:
            descendant, parent = query[0], query[1]
        except:
            break
        
        new_tree = find_parant(tree, parent)
        if find_descendant(new_tree, descendant):
            answer.append(2)
            query = sys.stdin.readline()[0:-1].split(" ")
            continue
        
        new_tree = find_parant(tree, descendant)
        if find_descendant(new_tree, parent):
            answer.append(1)
            query = sys.stdin.readline()[0:-1].split(" ")
            continue
        
        answer.append(0)
        query = sys.stdin.readline()[0:-1].split(" ")
        
    print(' '.join(map(str, answer)))
     
if __name__ == '__main__':
	main()