class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeSet:
    def __init__(self):
        self.root = None
        self.counter = 0
    def preorder(self, root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def add(self, value):
        self.root = self.add_helper(self.root, value)

    def add_helper(self, root, value):
        if root is None:
            return TreeNode(value)

        if value < root.value:
            root.left = self.add_helper(root.left, value)
        elif value > root.value:
            root.right = self.add_helper(root.right, value)

        return root

    def max(self):
        return self.max_helper(self.root)

    def max_helper(self, root):

        if root is None:
            return None

        if root.right is None:
            return root.value

        return self.max_helper(root.right)

    def min(self):
        return self.min_helper(self.root)

    def min_helper(self, root):
        if root is None:
            return None

        if root.left is None:
            return root.value

        return self.min_helper(root.left)

    def contains(self, find_val):
        return self.contains_helper(self.root, find_val)

    def contains_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.contains_helper(current.right, find_val)
            else:
                return self.contains_helper(current.left, find_val)

        else:
            return False

    def size(self):
        self.counter = 0
        return self.size_helper(self.root,self.counter)

    def size_helper(self, root, counter):
        if root is None:
            return self.counter

        self.counter += 1
        self.size_helper(root.left, counter)
        self.size_helper(root.right, counter)

        return self.counter


    def remove(self, value):
        self.root = self.remove_helper(self.root, value)

    def remove_helper(self, root, value):
        if root is None:
            return None

        if value < root.value:
            root.left = self.remove_helper(root.left, value)
        elif value > root.value:
            root.right = self.remove_helper(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.value = self.min_helper(root.right)
            root.right = self.remove_helper(root.right, root.value)

        return root

    def count(self, low, high):
        return self.count_helper(self.root, low, high)

    def count_helper(self, root, low, high):
        if root is None:
            return 0

        if root.value == high and root.value == low:
            return 1

        if root.value <= high and root.value >= low:
            return 1 + self.count_helper(root.left, low, high) + self.count_helper(root.right, low, high)

        elif root.value < low:
            return self.count_helper(root.right, low, high)

        else:
            return self.count_helper(root.left, low, high)