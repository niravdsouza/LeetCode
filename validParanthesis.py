class Solution(object):
    def isValid(self, s):
        stack = []
        for word in s:
            #print word
            if word == "{" or word == "[" or word == "(":
                stack.append(word)
            elif word == "}" or word == "]"or word == ")":
                if len(stack)==0:
                    return False
                if stack[len(stack)-1]=="{" and word == "}":
                    stack.pop()
                elif stack[len(stack)-1]=="[" and word == "]":
                    stack.pop()
                elif stack[len(stack)-1]=="(" and word == ")":
                    stack.pop()
                else:
                    return False
        if stack != []:
            return False
        #print "Valid String"
        return True
