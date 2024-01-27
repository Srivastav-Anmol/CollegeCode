class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    def is_balanced_fast(self, root):
        # Base case
        if not root:
            return True, 0

        left_balanced, left_height = self.is_balanced_fast(root.left)
        right_balanced, right_height = self.is_balanced_fast(root.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1

        return balanced, height

    def is_balanced(self, root):
        return self.is_balanced_fast(root)[0 ]

# You can implement your buildTree function in Python. For simplicity, let's assume you have it defined somewhere.
root = TreeNode(1)
root.left = TreeNode(10)
root.right = TreeNode(39)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.left=TreeNode(13)
root.is_balanced_fast(root)
print(root.is_balanced(root))
