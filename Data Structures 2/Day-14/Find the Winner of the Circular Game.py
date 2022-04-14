class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue=[]
		#add numbers (1 to n) in queue
        for i in range(1,n+1):
            queue.append(i)
		#declare counter variable
        c=1
        while(len(queue)!=1):
			#check if count==k and remove element and reinitialize count to 0
            if(c==k):
                queue.pop(0)
                c=1
			#otherwise remove the first element and append to the end of the queue
            else:
                queue.append(queue[0])
                queue.pop(0)
                c+=1
        return(queue[0])
