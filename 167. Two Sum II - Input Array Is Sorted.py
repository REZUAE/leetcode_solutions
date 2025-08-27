class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen ={}
        for i,n in enumerate(numbers):
            remainder = target - n
            if remainder in seen:
                return [seen[remainder]+1,i+1]
            seen[n] = i
        