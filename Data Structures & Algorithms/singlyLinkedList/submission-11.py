class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr_node = self.head
        pointer = 0
        while curr_node is not None and pointer <= index:
            if pointer == index:
                return curr_node.value
            pointer += 1
            curr_node = curr_node.next_node

        return -1

    def insertHead(self, val: int) -> None:
        if self.head is not None:
            self.head = LinkedListNode(val, self.head)
        else:
            self.head = LinkedListNode(val, None)

    def insertTail(self, val: int) -> None:
        curr_node = self.head
        if self.head is None:
            self.head = LinkedListNode(val, None)
        else:
            while curr_node is not None:
                if (not curr_node.has_next_node()):
                    curr_node.next_node = LinkedListNode(val, None)
                    break
                curr_node = curr_node.next_node

    def remove(self, index: int) -> bool:
        pointer = 0
        curr_node = self.head
        previous_node = self.head
        if (index == 0 and self.head is not None):
            if self.head.has_next_node():
                self.head = self.head.next_node
            else:
                self.head = None
            return True
        
        while curr_node is not None and pointer <= index:
            if (pointer == index - 1):
                if curr_node.has_next_node():
                    curr_node.next_node = curr_node.next_node.next_node
                    return True
                else:
                    return False
            else:
                curr_node = curr_node.next_node
                pointer += 1

        return False

    def getValues(self) -> List[int]:
        items = []
        curr_node = self.head
        while curr_node is not None:
            items.append(curr_node.value)
            curr_node = curr_node.next_node
        return items

class LinkedListNode:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def has_next_node(self):
        return self.next_node is not None