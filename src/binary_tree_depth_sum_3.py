class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def depth_sum(root: TreeNode, depth: int = 0) -> int:
    if root is None:
        return 0

    current_depth_sum = depth

    left_sum = depth_sum(root.left, depth + 1)
    right_sum = depth_sum(root.right, depth + 1)

    return current_depth_sum + left_sum + right_sum


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(7)
root.left.right = TreeNode(9)

print("Сума:", depth_sum(root))
