class Solution:
    def maxProduct(self, words: List[str]) -> int:
        count = 0
        
        for i in range(len(words)):
            set1 = set(words[i])
            for j in range(i+1, len(words)):
                if not set1.intersection(set(words[j])):
                    count = max(count, len(words[i])*len(words[j]))
                    
        return count
