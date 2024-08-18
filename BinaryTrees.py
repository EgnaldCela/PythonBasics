class BinaryNode:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

"""
Constructing our first tree
 
            1
          /    \
        2       3
      / \      / \ 
     4   5    6   7
    /
   8

"""
root = BinaryNode(1)
root.left = BinaryNode(2)
root.right = BinaryNode(3)
root.left.left = BinaryNode(4)
root.left.right = BinaryNode(5)
root.right.left = BinaryNode(6)
root.right.right = BinaryNode(7)
root.left.left.left = BinaryNode(8)


def count_nodes(root: BinaryNode) -> int:
    if root.left is None and root.right is None:  #base case: I am a single node
        return 1
    counter = 1
    if root.right is not None:
        counter += count_nodes(root.right)
    if root.left is not None:
        counter += count_nodes(root.left)
    return counter


print(f"Number of nodes: {count_nodes(root)}")


def count_leaves(root: BinaryNode) -> int:
    if root.right is None and root.left is None:
        return 1
    counter = 0
    if root.left is not None:
        counter += count_leaves(root.left)
    if root.right is not None:
        counter += count_leaves(root.right)
    return counter


print(f"Number of leaves: {count_leaves(root)}")


def sum_of_tree(root: BinaryNode) -> int:
    if root.right is None and root.left is None:
        return root.val
    sum = root.val
    if root.right is not None:
        sum += sum_of_tree(root.right)
    if root.left is not None:
        sum += sum_of_tree(root.left)
    return sum


print(f"Sum of the tree nodes: {sum_of_tree(root)}")


def height(root: BinaryNode) -> int:
    if root.right is None and root.left is None:
        return 1
    right_height, left_height = 1, 1
    if root.left is not None:
        left_height += height(root.left)
    if root.right is not None:
        right_height += height(root.right)
    return max(right_height, left_height)


# print(f"Height: {height(root)}")


def height_2(root: BinaryNode) -> int:  # different base case
    if root is None:
        return 0
    return 1 + max(height_2(root.left), height_2(root.right))


print(f"Height: {height_2(root)}")


def depth(root: BinaryNode) -> int:
    if root.right is None and root.left is None:
        return 0
    l,r = 1,1
    if root.right is not None:
        r +=  depth(root.right)
    if root.left is not None:
        l += depth(root.left)
    return max(l,r)


print(f"Depth: {depth(root)}")