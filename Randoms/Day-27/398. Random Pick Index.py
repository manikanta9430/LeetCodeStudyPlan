class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dict = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.dict[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.dict[target])
