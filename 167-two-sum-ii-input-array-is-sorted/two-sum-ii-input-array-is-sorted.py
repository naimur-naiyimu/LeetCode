class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while r > l:
            add = numbers[l] + numbers[r]
            if add == target:
                return [l+1, r+1]
            elif add > target:
                r -= 1
            elif add < target:
                l += 1
        