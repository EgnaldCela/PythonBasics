# from rtrace import TraceRecursion as trace
class TreeNode():
    def __init__(self, val, sons=None):
        self.val = val
        if sons is None:
            self.sons = []
        else:
            self.sons = sons  # TIP: You cannot pass mutable arguments to a function


"""
Logically we would expect the constructor to be

def __init__(self, val, sons = []):
    self.val = val
    self.sons = sons
    
BUT NO! We cannot pass lists as default values to a parameter in a function
( we cannot pass any mutable data type )    
"""
"""
             1
          /  |   \
        2    11    3
       /      | \ 
       4      6  7
    / | | \
   8  9 0  2
      |
      21
      
START CODING THE TREE BOTTOM - UP
"""
no21 = TreeNode(21)
root = TreeNode(9, [no21])
root = TreeNode(4, [TreeNode(8), root, TreeNode(0), TreeNode(2)])
no2 = TreeNode(2, [root])
no11 = TreeNode(11, [TreeNode(6), TreeNode(7)])
no3 = TreeNode(3)
root = TreeNode(1, [no2, no11, no3])


def count_nodes(root: TreeNode) -> int:
    if len(root.sons) == 0:
        return 1
    counter = 1
    for tree in root.sons:  # tree = son
        counter += count_nodes(tree)
    return counter


print(f"Number of nodes: {count_nodes(root)}")


def count_leaves(root: TreeNode) -> int:
    if len(root.sons) == 0:  # DO NOT USE if root.sons is None ... ( check constructor )
        return 1
    counter = 0
    for son in root.sons:
        counter += count_leaves(son)
    return counter


print(f"Number of leaves {count_leaves(root)}")


def sum(root: TreeNode) -> int:
    if len(root.sons) == 0:
        return root.val
    s = root.val
    for son in root.sons:
        s += sum(son)
    return s


print(f"Sum of tree: {sum(root)}")


def height(root: TreeNode) -> int:
    if len(root.sons) == 0:
        return 1
    h = []
    for son in root.sons:
        h.append(height(son))
    return max(h) + 1


print(f"Height: {height(root)}")


# @trace
def height2(root: TreeNode) -> int:  # neater !
    if len(root.sons) == 0:
        return 1
    return 1 + max([height(son) for son in root.sons])

# print(f"Height: {height2.trace(root)}")
