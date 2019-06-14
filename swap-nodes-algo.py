from copy import deepcopy
import sys
sys.setrecursionlimit(3500)

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

def find_idx(head, val):
    t = [head]
    while len(t) != 0:
        h = t.pop(0)

        if h.val == val:
            return h

        if h.left is not None:
            t.append(h.left)
        if h.right is not None:
            t.append(h.right)

def build_tree(tree_indexes):
    head = Node(1)
    for idx in range(len(tree_indexes)):
        pair = tree_indexes[idx]

        h = find_idx(head, idx + 1)

        if pair[0] != -1:
            h.left = Node(pair[0])
        if pair[1] != -1:
            h.right = Node(pair[1])
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

def tree_height(t):
    if t == None:
        return 0
    else:
        ld = tree_height(t.left)
        rd = tree_height(t.right)

        if ld > rd:
            return ld + 1
        return rd + 1

def swap_tree_at_multiple(t, query):
    k = 1
    while k*query < tree_height(t):
        swap_tree_at_layer(t, k*query)
        k += 1


def swapNodes(indexes, queries):
    t = build_tree(indexes)

    final = []
    for query in queries:
        swap_tree_at_multiple(t, query)
        result = []
        get_transverse(t, result)
        final.append(deepcopy(result))

    return final