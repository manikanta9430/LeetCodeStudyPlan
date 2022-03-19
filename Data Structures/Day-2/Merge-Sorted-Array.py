class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list1=[]
        list2=[]
        if m!=0:
            for i in range(m):
                list1.append(nums1[i])
        if n!=0:
            for i in range(n):
                list2.append(nums2[i])
        lis=list1+list2
        del nums1[:]
        for i in range(m+n):
            nums1.append(lis[i])
        nums1.sort()
