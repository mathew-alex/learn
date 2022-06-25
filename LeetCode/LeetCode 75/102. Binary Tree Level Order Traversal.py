'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

three = TreeNode(val=3)
nine = TreeNode(val=9)
twenty = TreeNode(val=20)
fifteen = TreeNode(val=15)
seven = TreeNode(val=7)

three.left = nine
three.right = twenty
twenty.left = fifteen
twenty.right = seven


class Solution:
    def levelOrder(self, root: TreeNode):
        if root == []:
            return []
        r = [[root.val]]
        s = [[root]]
        f = True
        while s and f:
            t = []
            st = []
            for i in s.pop(0):
                if i.left:
                    t.append(i.left.val)
                    st.append(i.left)
                if i.right:
                    t.append(i.right.val)
                    st.append(i.right)
            if t: r.append(t)
            if st: s.append(st)
            
        return r

print(Solution().levelOrder(three))