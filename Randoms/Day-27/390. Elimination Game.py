class Solution:
    def lastRemaining(self, n: int) -> int:
        
        #Each time either rule is executed
        #The difference between the numbers increases by a multiple of 2
        difference = 1;
        
        #Start is the first value of n and is always 1
        #The start will change depending on the rule applied
        start = 1;
        size = n;
        
        #We keep track of which rule to apply using this flag
        left_remove = True;
        
        
        #While we still have numbers to remove
        while size > 1:
            
            #We check and adjust parity of size
            isOdd = (size % 2 == 1);
            size = size - ceil( size / 2 );
            
            #If we are at the left rule, we increase the starting value
            #By the difference
            if left_remove:
                start += difference;
            #Otherwise, if we are at the right rule, 
            #Only when the size is odd do we adjust the start
            #By the difference
            elif isOdd and not left_remove:
                start += difference;
            #The difference increases each rule
            difference *= 2;
            #And we change the flag for the left rule each iteration
            left_remove = not left_remove;
            
        return start
