class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        pq=[];
        heappush(pq,1);
        dic={1:1};
        while(n):
            curr=heappop(pq);
            if(n==1):
                return curr
            for i in primes:
                new=i*curr;
                if(dic.get(new)):continue;
                dic[new]=1;
                heappush(pq,new);
            n-=1
