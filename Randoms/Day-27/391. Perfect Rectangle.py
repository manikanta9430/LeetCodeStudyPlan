class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        area = 0
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            bottom_left = (x1,y1) 
            upper_left = (x1,y2)
            bottom_right = (x2,y1)
            upper_right = (x2,y2)
            corners ^= {bottom_left, upper_left, bottom_right, upper_right}
            area += (y2 - y1) * (x2 - x1)
            
        if len(corners) != 4:
            return False 
        
        
        else:
            bottom_left = min(corners, key = lambda x: x[0] + x[1])
            upper_right = max(corners, key = lambda x: x[0] + x[1])
            return area == (upper_right[1] - bottom_left[1]) * (upper_right[0] - bottom_left[0])
