class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        no_lower = 1
        no_upper = 1
        no_num = 1
        
        repeating = []
        
        len_pass = len(password)
        streak = 1
        
        for i in range(len_pass):
            if password[i].islower():
                no_lower = 0
            if password[i].isupper():
                no_upper = 0
            if password[i].isnumeric():
                no_num = 0
                
            if i!=0 and password[i] == prev:
                streak +=1
            else:
                if streak > 2:
                    repeating.append(streak)
                streak = 1
            prev = password[i]
            
            if i==len_pass-1:
                if streak > 2:
                    repeating.append(streak)
        
        reminders = [x%3 for x in repeating]
        repeating = [x for _, x in sorted(zip(reminders, repeating))]
        reminders = [x%3 for x in repeating]
        
        dist_case = no_lower + no_upper + no_num
        dist = 0
        
        if len_pass < 6:
            dist = max(dist_case, 6-len_pass)
            
        if len_pass > 20:
            dist =  len_pass - 20
            while(dist>0 and reminders!=[]):
                for i, rem in enumerate(reminders):
                    if(rem<dist):
                        repeating[i] -= (rem+1)
                        dist -= rem+1
                    else:
                        repeating[i] -= dist
                        dist = 0
                        break
                reminders = [x%3 for x in repeating]
                repeating = [x for _, x in sorted(zip(reminders, repeating))]
                reminders = [x%3 for x in repeating]
            dist =  len_pass - 20
            len_pass = 20
            
        if len_pass >= 6 and len_pass <=20:
            dist_rep = 0
            for rep in repeating:
                dist_rep += int(rep/3//1)
            dist += max(dist_case, dist_rep)
        
        return dist
