from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
	
		#Count the frequency of each element and
		#store it in a dictionary
		
        d = defaultdict(int)
        for val in nums:
            d[val] += 1
		
		#Use heapq to heapify an array. heappush() will
		#add an element to the array as if it is a heap, and 
		#heappop() will remove the least element. In this case,
		#you must store the frequency and the element that
		#has that frequency in the priority queue. This requires 
		#putting tuples in the priority queue. heapq treats the 
		#first element of the tuple as the key for organizing
		#the priority queue.
		
        k_most_freq = []
        for key, val in d.items():
            if len(k_most_freq)==k:
                
				#checking if the current frequency 'val'
				#is greater than the least frequent element
				#in the priority queue.
				
                if val > k_most_freq[0][0]:
                        heapq.heappop(k_most_freq)
                        heapq.heappush(k_most_freq, (val, key))
                else:
                    continue

            else:
                heapq.heappush(k_most_freq, (val, key))
				
		#return the contents of the priority queue.
        return [pair[1] for pair in k_most_freq]
