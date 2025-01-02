class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0

        for lst in grid:
            l, r = 0, len(lst) - 1
            while l <= r:
                m = (l + r) // 2
                if lst[m] < 0:
                    # Check if this is the first negative number in the row
                    if m == 0 or lst[m - 1] >= 0:
                        # Add the count of negatives in this row
                        c += len(lst) - m
                        break
                    else:
                        # Search the left half for the first negative number
                        r = m - 1
                else:
                    # Search the right half
                    l = m + 1

        return c
