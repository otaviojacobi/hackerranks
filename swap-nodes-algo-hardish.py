from copy import deepcopy

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def get_transverse(head, result):
    if head == None:
        return

    get_transverse(head.left, result)
    result.append(head.val)
    get_transverse(head.right, result)

def build_tree(tree_indexes):
    if len(tree_indexes) == 0:
        return None

    mini = min(tree_indexes)
    minindex = tree_indexes.index(mini)
    head = Node(mini)

    head.set_left(build_tree(tree_indexes[:minindex]))
    head.set_right(build_tree(tree_indexes[minindex+1:]))

    return head

def get_next(tree_heads):
    new_heads = []
    for head in tree_heads:
        if head.left != None:
            new_heads.append(head.left)
        if head.right != None:
            new_heads.append(head.right)
    return new_heads


def swap_tree_at_layer(tree, layer):
    heads_at_layer = [tree]
    
    for _ in range(layer-1):
        heads_at_layer = get_next(heads_at_layer)

    for head in heads_at_layer:
        head.left, head.right = head.right, head.left

def swapNodes(indexes, queries):
    t = build_tree(indexes)

    final = []
    for query in queries:
        swap_tree_at_layer(t, query)
        result = []
        get_transverse(t, result)
        final.append(deepcopy(result))

    return final

print(swapNodes([6, 9, 4, 2, 1, 7, 5, 10, 8, 11, 3],[2,4]))