class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left_child = None
        self.right_child = None


class PriorityQueue:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, current_node, new_node):
        if new_node.priority <= current_node.priority:
            if current_node.left_child is None:
                current_node.left_child = new_node
            else:
                self._insert_recursive(current_node.left_child, new_node)
        else:
            if current_node.right_child is None:
                current_node.right_child = new_node
            else:
                self._insert_recursive(current_node.right_child, new_node)

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _find_highest_priority(self, current_node):
        if current_node.right_child is None:
            return current_node
        return self._find_highest_priority(current_node.right_child)

    def delete_highest_priority(self):
        if self.root is None:
            return None
        highest_priority_node = self._find_highest_priority(self.root)
        if highest_priority_node == self.root:
            self.root = self.root.left_child
        else:
            parent = self.root
            while parent.right_child != highest_priority_node:
                parent = parent.right_child
            parent.right_child = highest_priority_node.left_child
        return highest_priority_node.value

    def view(self):
        if not self.root:
            print("empty")
            return

        current_level = [self.root]
        while current_level:
            next_level = []
            for node in current_level:
                print(f"Value: {node.value}, Priority: {node.priority}")
                if node.left_child:
                    next_level.append(node.left_child)
                if node.right_child:
                    next_level.append(node.right_child)
            current_level = next_level
