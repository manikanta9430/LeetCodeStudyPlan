class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 15 == 0:
                res.append("FizzBuzz")
                continue
            elif i % 3 == 0:
                res.append("Fizz")
                continue
            elif i % 5 == 0:
                res.append("Buzz")
                continue
            else:
                res.append(str(i))
                continue
        return res
