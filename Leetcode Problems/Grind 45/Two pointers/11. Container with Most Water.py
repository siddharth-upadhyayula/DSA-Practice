class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxarea = 0

        while l<r:
            if (r-l)*(min(height[l],height[r]))>maxarea:
                maxarea = (r-l)*(min(height[l],height[r]))
            l+=1
        return maxarea