from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> list[list[int]]:
    res = []
    queue = deque([root])
    while len(queue) > 0:
        n = len(queue)
        new_level = []
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
        res.append(new_level)
    return res

def build_tree(nodes):
    """
    Constrói uma árvore binária a partir de uma lista de valores usando ordem nível (None representa ausência de nó).
    Exemplo: [1, 2, 3, None, 4] gera uma árvore onde 2 não tem filho esquerdo mas tem filho direito 4.
    """
    if not nodes or nodes[0] is None:
        return None
    it = iter(nodes)
    root = Node(next(it))
    queue = deque([root])
    for val in it:
        current = queue.popleft()
        if val is not None:
            current.left = Node(val)
            queue.append(current.left)
        try:
            val = next(it)
            if val is not None:
                current.right = Node(val)
                queue.append(current.right)
        except StopIteration:
            break
    return root

if __name__ == "__main__":
    # Exemplo de input: 1 2 3 None 4 None None
    raw = input("Digite os nós da árvore (use None para ausente): ").split()
    nodes = [int(x) if x != "None" else None for x in raw]
    tree = build_tree(nodes)
    resultado = level_order_traversal(tree)
    print(resultado)
