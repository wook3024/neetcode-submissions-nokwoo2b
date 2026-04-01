# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 
        def find_max(cur, node):
            if node == None:
                return cur
            if node.left == None and node.right == None:
                return cur

            left_max = right_max = 0
            cur_diameter = 0
            if node.left != None:
                print(f"node.left {node.left.val, cur}")
                left_max = max(find_max(cur + 1, node.left), cur)
                cur_diameter += left_max - cur
            if node.right != None:
                print(f"node.right {node.right.val, cur}")
                right_max = max(find_max(cur + 1, node.right), cur)
                cur_diameter += right_max - cur

            nonlocal diameter
            diameter = max(diameter, cur_diameter)
            
            return max(left_max, right_max)

        if root == None:
            return 0
        
        find_max(0, root)

        # diameter = 0
        # if root.left != None:
        #     diameter += find_max(0, root.left) + 1
        # if root.right != None:
        #     diameter += find_max(0, root.right) + 1
        
        return diameter
        # leaf_list = [root]

        # def find_leaf(node):
        #     if node == None:
        #         return

        #     if node.left == None and node.right == None:
        #         leaf_list.append(node)

        #     if node.left != None:
        #         find_leaf(node.left)
        #     if node.right != None:
        #         find_leaf(node.right)

        # def find_max(cur, node, checked):
        #     if node.val in checked:
        #         return cur - 1
        #     checked.append(node.val)
            
        #     if node.left == None and node.right == None:
        #         print(f"find_max {node.val, cur}")
        #         return cur - 1

        #     cur_max = 0
        #     if node.left != None:
        #         print(f"node.left {node.left.val, cur}")
        #         cur_max = max(find_max(cur + 1, node.left, checked), cur_max)
                
        #     if node.right != None:
        #         print(f"node.right {node.right.val, cur}")
        #         cur_max = max(find_max(cur + 1, node.right, checked), cur_max)
                
                
        #     return cur_max


        # find_leaf(root)
        # print(leaf_list)

        # diameter = 0
        # for leaf in leaf_list:
        #     diameter = max(diameter, find_max(1, leaf, []))
        #     print(f"leaf_check {leaf.val, diameter}")

        return diameter


