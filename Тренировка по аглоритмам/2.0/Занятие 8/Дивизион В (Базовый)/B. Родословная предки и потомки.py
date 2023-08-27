import sys

def main():
    '''
    '''
    def find_first_parant(parant_set, descendant_set):
        for parent in parant_set:
            if not (parent in descendant_set):
                return parent
    
    def create_tree(parent, parant_child_dict):
        tree = [parent, []]
        for descendant in parant_child_dict[parent]:
            tree[1].append(add_descendant(descendant, parant_child_dict))
        return tree
    
    def add_descendant(parent, parant_child_dict):
        if not (parent in parant_child_dict):
            return [parent, []]
        else:
            tree = [parent, []]
            for descendant in parant_child_dict[parent]:
                tree[1].append(add_descendant(descendant, parant_child_dict))
            return tree
    
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
    parant_child_dict = {}
    descendant_set = set()
    parent_set = set()
    for i in range(N-1):
        descendant, parent = input().split()
        descendant_set.add(descendant)
        parent_set.add(parent)
        
        if parent not in parant_child_dict:
            parant_child_dict[parent] = []
        parant_child_dict[parent].append(descendant)        

    parent = find_first_parant(parent_set, descendant_set)
    tree = create_tree(parent, parant_child_dict)

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