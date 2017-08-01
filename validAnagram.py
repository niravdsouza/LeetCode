class Solution(object):
    def isAnagram(self, s, t):
        a1=list(s)
        a2=list(t)
        dic={}
        for element in a1:
            if element in dic:
                dic[element]+=1
            else:
                dic[element]=1
        for element in a2:
            if element in dic:
                if dic[element]==1:
                    del(dic[element])
                else:
                    dic[element]-=1
            else:
                return False
        if dic=={}:
            return True
        else:
            return False
