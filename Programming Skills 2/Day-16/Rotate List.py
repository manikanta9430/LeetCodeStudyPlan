class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # If len(linkedlist) is 0 or 1 , we simply return the head as
        # it does not affect the answer
        if not head or not head.next:
            return head
        
        # To get length of linked list
        def getlen(node):
            c=0
            while node:
                c+=1 
                node=node.next 
            return c
        
        k=k%getlen(head) # Decreasing the number of rotations
        
        
        #rotating linkedlist by 1 in each step
        while k:
            
            node=head
            
            #We make temp for iterating purpose
            temp=node
            
            # Iterating until we reach the second last node
            while temp.next.next:
                temp=temp.next 
                
            # Storing the last node
            last=temp.next
            
            #Making secondlastnode.next=None
            temp.next=None 
            
            #Putting all elements ahead of the last node
            last.next=node
            
            #For next iteration we make head equal to the current rotated linkedlist
            head=last
            k-=1
            
            
        return head
