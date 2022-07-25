class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        for i in range(0, len(nums), 2):
            print(nums[i:i+2])
            answer += min(nums[i:i+2])
        return answer