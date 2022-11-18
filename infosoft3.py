class Node():
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        if node.start >= self.end:
            if self.left_child is None:
                self.left_child = node
                return True
            return self.left_child.insert(node)
        elif node.end <= self.start:
            if self.right_child is None :
                self.right_child = node
                return True
            return self.right_child.insert(node)
        else:
            return False

class Calendar():
    def __init__(self):
        self.root: Node = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start=start, end=end)
            return True
        return self.root.insert(node=Node(start, end))
    
        
        
calendar = Calendar()
print(calendar.book(5, 10))
print(calendar.book(8, 13)) 
print(calendar.book(10, 15)) 