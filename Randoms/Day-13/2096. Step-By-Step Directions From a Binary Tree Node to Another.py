class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        

        found_path = False
        all_steps = ""
        # 0 found start
        # 1 found dest
        def traverse_tree(node):
            if node is None:
                return (-1,"")
            
            nonlocal found_path , all_steps,destValue,startValue
            if found_path:
                return -1,""

            found_in_left,l_steps = traverse_tree(node.left)
            found_in_right,r_steps = traverse_tree(node.right)
            # print(node.val,found_in_left,l_steps,found_in_right,r_steps)
            
            if found_in_left == 0:
                l_steps += "U"
            elif found_in_left == 1:
                l_steps = "L" + l_steps
            
            if found_in_right == 0:
                r_steps += "U"
            elif found_in_right == 1:
                r_steps = "R" + r_steps
                
            if node.val != destValue and node.val != startValue:
                if found_in_left >= 0 and found_in_right >= 0:
                    path = l_steps + r_steps if found_in_left == 0 else r_steps + l_steps
                    all_steps = path
                    found_path = True
                    return -1,""
                elif found_in_left == -1 and found_in_right == -1:
                    return -1,""
                else:
                    return (found_in_left,l_steps) if found_in_left >= 0 else (found_in_right,r_steps)
            
            elif node.val == destValue:
                if found_in_left == 0 or found_in_right ==0:
                    found_path = True
                    all_steps = l_steps if found_in_left ==0 else r_steps
                    return -1,""
                return 1,""
            
            else:
                if found_in_left == 1 or found_in_right == 1:
                    found_path = True
                    all_steps = l_steps if found_in_left ==1 else r_steps
                    return -1,""
                return 0,""   
        
        traverse_tree(root)
        return all_steps
