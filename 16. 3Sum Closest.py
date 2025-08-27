class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")

        for i in range(len(nums)-2):
            L = i+1
            R = len(nums)-1
            while L < R:
                total = nums[R] + nums[L] + nums[i]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    L+=1

                elif total > target:
                    R-=1

                else:
                    return target
        return closest