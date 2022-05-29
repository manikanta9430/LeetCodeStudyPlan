class Solution:
    def reconstructQueue(self, pe: List[List[int]]) -> List[List[int]]:
        l = [[-1,-1] for i in range(len(pe))]
        pe.sort()
        for i in range(len(pe)):
            c = pe[i][1]
            for j in range(len(pe)):
                if c>0:
                    if l[j][0] != -1:
                        if l[j][0] >= pe[i][0]:
                            c -= 1
                        else:
                            continue
                    else:
                        c -= 1
                else:
                    if l[j][0] == -1:
                        l[j] = pe[i]
                        break
        return l
