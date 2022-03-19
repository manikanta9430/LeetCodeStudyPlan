class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        salary.sort(reverse=True)
        sum =0
        for i in range(1,n-1):
            sum += salary[i]
        #sum = sum - salary[1]-salary[-1]
        return sum/(n-2)
        
