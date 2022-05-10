class Solution(object):
    def convertToTitle(self, columnNumber):
        if columnNumber <= 26:
            return chr(ord('A') + columnNumber - 1)
        else:
            return self.convertToTitle((columnNumber-1)//26) + self.convertToTitle((columnNumber-1)%26+1)
