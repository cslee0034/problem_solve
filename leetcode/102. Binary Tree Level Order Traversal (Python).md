# 102. Binary Tree Level Order Traversal (Python)

## Source

https://leetcode.com/problems/binary-tree-level-order-traversal/description/

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        def traverse(root: Optional[TreeNode], dept: int):
            dept += 1

            if root is None:
                return

            if (len(answer) <= dept):
                for i in range(dept - len(answer) + 1):
                    answer.append([])
            answer[dept].append(root.val)
            traverse(root.left, dept)
            traverse(root.right, dept)

        traverse(root, -1)
        return answer
```

## How to solve?

1. answer의 초기화를 막기 위해 내부 함수로 traverse를 선언하고 answer은 외부 함수에 선언한다.

2. [[]] 같은 중복된 리스트의 내부 깊이를 구현하기 위해 dept 변수를 선언하고 매 recursion마다 dept를 1씩 추가 해준다.

3. 만약 answer의 배열의 길이가 dept보다 작거나 같다면 그 차이만큼 빈 배열을 선언 해준다.

4. answer의 dept의 깊이에 해당하는 배열에 값을 추가 해준다.

5. 순서대로 트리를 순회 해준다.
