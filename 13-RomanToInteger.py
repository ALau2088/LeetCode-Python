"""
#IOCE

I: roman numeral(str)
O: value(int)
C: none
E: empty string

#Examples/Explanation
Input: II
Output: 2
1. Iterate through letters in str
I -> 1
I -> 1
2. Add Value
1 + 1 = 2

Input: IV
Output: 4
1. Iterate through letters in str
IV -> 4 requires check if next letter is V

Similar cases
-IX
-XL
-XC
-CD
-CM


# Pseudocode

// Edge case-empty string
// IF length of string is 0 return 0

// romanNumeralLookUpObj(rnluo)
// romanNumeralValueInt(rnvi)

// FOR letter in str:
  // IF letter is I AND next letter is V add 4 to rnvi
  // ELSE IF letter is I AND next letter is X add 9 to rnvi
  // ELSE IF letter is X AND next letter is L add 40 to rnvi
  // ELSE IF letter is X AND next letter is C add 90 to rnvi
  // ELSE IF letter is C AND next letter is D add 400 to rnvi
  // ELSE IF letter is C AND next letter is M add 900 to rnvi
  // ELSE look up value of letter in rnluo and then add value to rnvi
// RETURN rnvi
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0

        rnluo = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        rnvi = 0
        for i in range(len(s)):
            # conditions for skipping iteration
            if (i > 0):
                if(s[i] == 'V' and s[i-1] == 'I'):
                    continue
                if(s[i] == 'X' and s[i-1] == 'I'):
                    continue
                if(s[i] == 'L' and s[i-1] == 'X'):
                    continue
                if(s[i] == 'C' and s[i-1] == 'X'):
                    continue
                if(s[i] == 'D' and s[i-1] == 'C'):
                    continue
                if(s[i] == 'M' and s[i-1] == 'C'):
                    continue

            if(i != len(s) - 1):
                if s[i] == 'I' and s[i+1] == 'V':
                    rnvi += 4
                elif s[i] == 'I' and s[i+1] == 'X':
                    rnvi += 9
                elif s[i] == 'X' and s[i+1] == 'L':
                    rnvi += 40
                elif s[i] == 'X' and s[i+1] == 'C':
                    rnvi += 90
                elif s[i] == 'C' and s[i+1] == 'D':
                    rnvi += 400
                elif s[i] == 'C' and s[i+1] == 'M':
                    rnvi += 900
                else:
                    rnvi = rnvi + rnluo[s[i]]
            else:
                rnvi = rnvi + rnluo[s[i]]
        return rnvi

"""
Alternative Solution

def romanToInt(self, s: str) -> int:
	res, prev = 0, 0
	dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	for i in s[::-1]:          # rev the s
		if dict[i] >= prev:
			res += dict[i]     # sum the value iff previous value same or more
		else:
			res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
		prev = dict[i]
	return res

"""