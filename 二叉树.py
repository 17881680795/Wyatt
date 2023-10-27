# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-03-23
# @FileName: 二叉树.py
"""
python二叉树可以用在哪些地方？
1.  数据库索引：二叉树可以用于数据库的索引结构，可以快速地进行查询、插入和删除操作。

2.  文件系统：文件系统的目录结构可以用二叉树来实现，每个节点代表一个目录或文件。

3.  编译器：语法分析阶段可以使用二叉树来构建语法树，以便进行后续的编译操作。

4.  人工智能：决策树和神经网络是二叉树的一种形式，可以用于训练和运行机器学习模型。

5.  哈夫曼编码：哈夫曼编码是一种基于二叉树的数据压缩算法，可以有效地压缩数据。

6.  游戏开发：游戏中的场景和人物可以用二叉树来表示，便于进行碰撞检测、寻路等操作。

7.  数据结构算法：二叉树是计算机科学中最基本的数据结构之一，可以用于实现很多算法，如排序、查找、遍历等。

总之，二叉树可以用在各种需要组织和管理数据的场景中，具有广泛的应用价值。



二叉树怎么理解？
Python二叉树是一种数据结构，它由节点组成，每个节点最多有两个子节点，分别称为左子节点和右子节点，使之成为一个树形结构。

在Python二叉树中，每个节点包含一个值和指向其左右子节点的指针。这些节点被称为二叉搜索树或BST，其中每个节点的左子树节点小于它，右子树节点大于它。

通过Python二叉树，可以轻松搜索值，从而提高查找效率。Python中的二叉树在处理大量数据时具有较高的效率，并且易于在程序中实现。


1.  先了解二叉树的基本概念和特点，了解二叉树的遍历方式，包括前序、中序、后序遍历以及层次遍历等。

2.  通过画图和模拟实现二叉树的基本操作，如插入节点、删除节点和查找节点等。这样可以更清晰地理解二叉树的结构和操作。

3.  学习  Python  内置的  collections  模块中的二叉树函数，例如  binary_tree  和  heap。了解它们的功能和用法，可以提高二叉树的使用效率。

4.  总结和归纳二叉树的性质和规律，例如二叉搜索树的性质、平衡二叉树的性质等。这些知识点的掌握可以帮助更好地设计和优化二叉树的算法。

5.  阅读相关的  Python  二叉树实现代码和文章，了解其他人的使用经验和观点。这样可以帮助发现更多的应用场景和解决问题的思路。
"""


# class Node:
#     def __init__(self, datasets):
#         self.left = None
#         self.right = None
#         self.datasets = datasets
#
#     def insert(self, datasets):
#         if self.datasets:
#             if datasets < self.datasets:
#                 if not self.left:
#                     self.left = Node(datasets)
#                 else:
#                     self.left.insert(datasets)
#             elif datasets > self.datasets:
#                 if not self.right:
#                     self.right = Node(datasets)
#                 else:
#                     self.right.insert(datasets)
#         else:
#             self.datasets = datasets
#
#     def print_tree(self):
#         if self.left:
#             self.left.print_tree()
#         print(self.datasets)
#         if self.right:
#             self.right.print_tree()
#
#
# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
#
# root.print_tree()


# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#
# class Binary_Tree(object):
#     def __init__(self, root):
#         self.root = Node(root)
#
#     def insert(self, value):
#         """插入函数"""
#         node = Node(value)
#         if self.root is None:
#             self.root = node
#         else:
#             self._insert(value, self.root)
#
#     def _insert(self, value, cur_node):
#         if value < cur_node.value:
#             if cur_node.left_child is None:
#                 cur_node.left_child = Node(value)
#             else:
#                 self._insert(value, cur_node.left_child)
#         elif value > cur_node.value:
#             if cur_node.right_child is None:
#                 cur_node.right_child = Node(value)
#             else:
#                 self._insert(value, cur_node.right_child)
#
#     def search(self, value):
#         """搜索函数"""
#         if self.root is None:
#             return False
#         else:
#             return self._search(value, self.root)
#
#     def _search(self, value, cur_node):
#         if value == cur_node.value:
#             return True
#         elif value < cur_node.value and cur_node.left_child is not None:
#             return self._search(value, cur_node.left_child)
#         elif value > cur_node.value and cur_node.right_child is not None:
#             return self._search(value, cur_node.right_child)
#         else:
#             return False
#
#     def print_tree(self, traversal_type):
#         """遍历函数"""
#         if traversal_type == "inorder":
#             return self.inorder_print(self.root, "")
#         elif traversal_type == "preorder":
#             return self.preorder_print(self.root, "")
#         elif traversal_type == "postorder":
#             return self.postorder_print(self.root, "")
#         else:
#             print("Traversal  type  " + str(traversal_type) + "  is  not  supported.")
#             return False
#
#     def inorder_print(self, start, traversal):
#         if start:
#             traversal = self.inorder_print(start.left_child, traversal)
#             traversal += str(start.value) + "-"
#             traversal = self.inorder_print(start.right_child, traversal)
#         return traversal
#
#     def preorder_print(self, start, traversal):
#         if start:
#             traversal += str(start.value) + "-"
#             traversal = self.preorder_print(start.left_child, traversal)
#             traversal = self.preorder_print(start.right_child, traversal)
#         return traversal
#
#     def postorder_print(self, start, traversal):
#         if start:
#             traversal = self.postorder_print(start.left_child, traversal)
#             traversal = self.postorder_print(start.right_child, traversal)
#             traversal += str(start.value) + "-"
#         return traversal
#
#
# #  创建一个二叉树
# tree = Binary_Tree(4)
#
# #  插入节点
# tree.insert(2)
# tree.insert(1)
# tree.insert(3)
# tree.insert(5)
#
# #  查找节点
# print(tree.search(4))  # True
# print(tree.search(6))  # False
#
# #  遍历二叉树
# print(tree.print_tree("inorder"))  # 1-2-3-4-5-
# print(tree.print_tree("preorder"))  # 4-2-1-3-5-
# print(tree.print_tree("postorder"))  # 1-3-2-5-4-


"""
可以使用递归来实现遍历二叉树的操作。有三种遍历顺序：

1.  前序遍历（pre-order  traversal）：访问根节点、访问左子树、访问右子树
2.  中序遍历（in-order  traversal）：访问左子树、访问根节点、访问右子树
3.  后序遍历（post-order  traversal）：访问左子树、访问右子树、访问根节点
"""






# # 定义节点类
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
#
# def preorder_traversal(node):
#     if node is not None:
#         print(node.val)
#         preorder_traversal(node.left)
#         preorder_traversal(node.right)
#
#
# def iterative_preorder_traversal(root):
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node is not None:
#             print(node.val)
#             stack.append(node.right)
#             stack.append(node.left)





# 定义二叉树节点类
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 定义二叉树类
class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    # 前序遍历
    def preorder_traversal(self, tree_node):
        if tree_node:
            print(tree_node.value)
            self.preorder_traversal(tree_node.left)
            self.preorder_traversal(tree_node.right)

    # 中序遍历
    def inorder_traversal(self, tree_node):
        if tree_node:
            self.inorder_traversal(tree_node.left)
            print(tree_node.value)
            self.inorder_traversal(tree_node.right)

    # 后序遍历
    def postorder_traversal(self, tree_node):
        if tree_node:
            self.postorder_traversal(tree_node.left)
            self.postorder_traversal(tree_node.right)
            print(tree_node.value)


# 测试代码
if __name__ == '__main__':
    # 创建二叉树
    bt = BinaryTree(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    bt.root.left.left = TreeNode(4)
    bt.root.left.right = TreeNode(5)

    # 前序遍历输出结果: 1 2 4 5 3
    bt.preorder_traversal(bt.root)

    # 中序遍历输出结果: 4 2 5 1 3
    bt.inorder_traversal(bt.root)

    # 后序遍历输出结果: 4 5 2 3 1
    bt.postorder_traversal(bt.root)
