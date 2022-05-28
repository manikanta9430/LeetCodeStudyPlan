class Solution(object):
    
    #Method needed to convert data into encoding
    def eightBit(self,num):
            result = ""
            while num >0:
                result = str(num % 2) + result
                num = num//2
            zeros = 8 - len(result)
            while zeros > 0:
                result = "0" + result
                zeros -= 1
            return result
    
    
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        string = ""
        for i in data:
            string = string + self.eightBit(i)
        #We need to validate this string
        chunks = 0
        while chunks < len(string):
            temp = string[chunks : chunks + 8]
            if temp[0] == "0":
                chunks +=8
            elif temp[0:3] == "110":
                if (chunks + 8) < len(string):
                    if (string[chunks + 8 : chunks + 16])[0:2] != "10":
                        return False
                    else:
                        chunks +=16
                else:
                    return False
            elif temp[0:4] == "1110":
                if (chunks + 16) < len(string):
                    temp2 = string[chunks+8 : chunks + 16]
                    temp3 = string[chunks + 16 : chunks + 24]
                    if temp2[0:2] != "10" or temp3[0:2] != "10":
                        return False
                    else:
                        chunks += 24
                else:
                    return False
            elif temp[0:5] == "11110":
                if (chunks + 24) < len(string):
                    temp2 = string[chunks+8 : chunks + 16]
                    temp3 = string[chunks + 16 : chunks + 24]
                    temp4 = string[chunks + 24:chunks + 32]
                    if temp2[0:2] != "10" or temp3[0:2] != "10" or temp4[0:2] != "10":
                        return False
                    else:
                        chunks +=32
                else:
                    return False
            else:
                return False
        return True

