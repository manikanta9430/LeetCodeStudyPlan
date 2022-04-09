class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        
        for i in strs:
            if str(sorted(i)) in mydict:
                mydict[str(sorted(i))] += [i]
            else:
                mydict[str(sorted(i))] = [i]
        return mydict.values()
