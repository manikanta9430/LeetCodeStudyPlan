#MyApproach, but dont know why getting wrong o/p
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[len(nums1)]
        for x in nums1:
            for i in range(len(nums2)):
                if (x==nums2[i]):
                    if(i==len(nums2)-1):
                        ans.append(-1)
                    else:
                        ans.append(nums2[i+1])
        return ans
   
#Lets Explore Random solution for this.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        n = len(nums2)
        st = []
        for i in range(n-1, -1, -1):
            while st and st[-1] <= nums2[i]:
                st.pop()
            if st:
                ans[nums2[i]] = st[-1]
            st.append(nums2[i])
            
        return [ans.get(num, -1) for num in nums1]
