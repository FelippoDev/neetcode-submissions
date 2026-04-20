class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None


class MinStack:
    def __init__(self):
        self._top = None
        self.length = 0
        self._min = []
    
    def push(self, val: int) -> None:
        node = Node(val)
        if not self._top:
            self._top = node
            self._min.append(node.value)
        else:
            node.next_value = self._top
            self._top = node
            self._min.append(node.value)

        self.length += 1

    def pop(self):
        self._top = self._top.next_value
        self.length -= 1 if self.length != 0 else 0
        self._min.pop()
    
    def top(self):
        return self._top.value
    
    def getMin(self):
        return min(self._min)