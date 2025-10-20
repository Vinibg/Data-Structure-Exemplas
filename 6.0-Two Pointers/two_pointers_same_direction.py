class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val

def build_list(nodes, f):
    # Função não está completa na imagem. Implemente conforme sua necessidade.
    pass

if __name__ == "__main__":
    # Código principal não está visível na imagem. Implemente conforme sua lógica.
    pass
