from typing import Dict, List, Optional, Tuple

null = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Convert List to ListNode
def list_to_listnode(target: List[int]) -> ListNode:
    result = current_node = ListNode()
    for each in target:
        current_node.next = ListNode(val=each)
        current_node = current_node.next
    return result.next


# Convert ListNode to List
def listnode_to_list(listnode: ListNode) -> List[int]:
    result = []
    while listnode.next:
        result.append(listnode.val)
        listnode = listnode.next
    result.append(listnode.val)
    return result


# Convert List to TreeNode
def list_to_treenode(data: List[int], index: int = 0) -> Optional[TreeNode]:
    result = None
    if index < len(data):
        if data[index] is not None:
            result = TreeNode(data[index])
            result.left = list_to_treenode(data, 2 * index + 1)
            result.right = list_to_treenode(data, 2 * index + 2)
        else:
            return None
    return result


def treenode_to_list(treenode: TreeNode) -> List[int]:
    items = []
    queue = [treenode]

    while queue:
        copy = queue[:]
        queue = []

        for item in copy:
            if item is None:
                items.append(None)
                queue.append(None)
                queue.append(None)
            else:
                items.append(item.val)
                queue.append(item.left)
                queue.append(item.right)

        if all((x is None for x in queue)):
            break
    return items
