
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function for recursive reversal
        def reverse_recursive(node, prev):
            if not node:
                return prev

            next_node = node.next
            node.next = prev

            return reverse_recursive(next_node, node)

        return reverse_recursive(head, None)