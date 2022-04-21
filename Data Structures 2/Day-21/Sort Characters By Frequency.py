class Solution:
    def frequencySort(self, s: str) -> str:
        data = Counter(s)
        data = sorted(data.items(), key=lambda x:-x[1])
        ans=''
        for i in data:
            ans += i[0]*i[1]
        return ans
