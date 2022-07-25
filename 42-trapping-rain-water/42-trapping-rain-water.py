class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        water = 0
        max_height = height.index(max(height))
        max_left, max_right = 0, 0
        
        while (left < right):
            if left < max_height:
                max_left = max(height[left], max_left)
                if (height[left+1] < max_left):
                    water += (max_left-height[left+1])
                left += 1
            
            if right > max_height:
                max_right = max(height[right], max_right)
                if (height[right-1] < max_right):
                    water += (max_right-height[right-1])
                right -= 1
            
        return water
            
            
            
            
            
            
        