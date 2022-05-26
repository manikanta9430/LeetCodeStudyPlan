class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        result=[]
        maxHeap=[]
        heapq.heapify(maxHeap)
        
        for i in range(min(k,len(nums1))):
            for j in range(min(k,len(nums2))):
                if len(maxHeap)<k:
                    heapq.heappush(maxHeap,(-(nums1[i]+nums2[j]),nums1[i],nums2[j]))
                else:
                    if nums1[i]+nums2[j] > -maxHeap[0][0]:
                        break
                    
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap,(-(nums1[i]+nums2[j]),nums1[i],nums2[j]))
        print(maxHeap)
        
        for i in range(len(maxHeap)):
            result.append([maxHeap[i][1],maxHeap[i][2]])
        
        return result
