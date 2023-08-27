def main():
    '''
    '''
    def add_descendant(tree, parent, descendant):
        if parent == tree[0]:
            descendant_tree = [descendant, []]
            tree[1].append(descendant_tree)
            return True
        else:
            for child in tree[1]:
                if add_descendant(child, parent, descendant):
                    return True
    
    N = int(input())
    descendant, parent = input().split()
    descendant_tree = [descendant, []]
    tree = [parent, [descendant_tree]]
    for i in range(N-2):
        descendant, parent = input().split()
        if add_descendant(tree, parent, descendant):
            continue
        else:
            print("ERROR")
     
if __name__ == '__main__':
	main()