'''
#IOCE
I: string of parentheses(str)
O: (bool):true if brackets are valid
C: none
E: 1-empty string is valid,2-invalid when there is right bracket and no left bracket

#Examples
Input:"()"
Output: true

Step1: keep track of left bracket types
Step2: if right bracket check if it closes last left bracket, if yes remove last left bracket and continue, else false
Step3: When iterated thru every character in string and there are no more left brackets, string is valid 

#PseudoCode
// leftBrackets(arr)
// FOR chars of string: 
    // IF char is left bracket ADD to leftBrackets
    //ELSE IF it a right bracket AND there is a left bracket AND closes the last left brack: 
      // remove the last left bracket
      // continue
    //ELSE return false
// if there are no more leftBrackets return true:
    //RETURN true
// else RETURN false
    
'''


class Solution:
    def isValid(self, s: str) -> bool:
        # Edge case-empty string
        if len(s) == 0:
            return True

        lb = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                lb.append(char)
            elif len(lb) > 0:
                if lb[len(lb)-1]+char == '()' or lb[len(lb)-1]+char == '{}' or lb[len(lb)-1]+char == '[]':
                    lb.pop(len(lb) - 1)
                else:
                    return False
                continue
            else:
                return False

        if len(lb) == 0:
            return True
        else:
            return False


Solution = Solution()
print(Solution.isValid(']'))
