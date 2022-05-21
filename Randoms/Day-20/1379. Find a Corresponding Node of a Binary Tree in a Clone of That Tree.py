class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        #Edge case
        if original is None:
            return None;
        
        #Current path will be what we track in our depth first search (dfs)
        current_path = []
        #Solution path is how we will save our solution in a lazy way
        #Lists are mutable and will keep changes during our recursive call
        soln_path = [ None ]
        
        #DFS on the original to see what the path will be
        self.dfs( original, target, current_path, soln_path )
        
        #Go to the root of the cloned tree
        soln_pointer = cloned

        #For each path command toward the correct node
        #We follow the commands to arrive at the twin in the cloned tree
        for path_command in soln_path[ 0 ]:
            if path_command == 'left':
                soln_pointer = soln_pointer.left
            elif path_command == 'right':
                soln_pointer = soln_pointer.right
            else:
                raise ValueError('bad command passed to soln_path')
                exit( 7 )
        return soln_pointer
    
    def dfs( self, root, target, current_path, soln_path ):
        
        #Check if we have found the solution
        solution_exists = soln_path[ 0 ] is not None
        
        if solution_exists:
            return
        
        #Look at the children
        left_child = root.left
        right_child = root.right
        
        #If the current root is the target node, we copy the
        #current_path to our mutable list
        if root is target:
            soln_path[ 0 ] = current_path.copy()
            return current_path.copy()
          
        #If we have not found the solution, we search the left
        #child
        if left_child is not None:
            current_path.append( 'left' )
            self.dfs( left_child, target, current_path, soln_path )
            current_path.pop()
            
        #Checking again to avoid unnecessary calls 
        #In case the solution was found already in the other recursive call
        solution_exists = soln_path[ 0 ] is not None
        
        if right_child is not None and not solution_exists:
            current_path.append( 'right' )
            self.dfs( right_child, target, current_path, soln_path )
            current_path.pop()
