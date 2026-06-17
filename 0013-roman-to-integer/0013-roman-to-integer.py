class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_value_map = {"I":1,"V":5,"X":10,"L":50,"C":100, "D":500, "M":1000}
        number = 0
        l = len(s)
        if len(s)< 2:
            return symbol_to_value_map.get(s)
        i = l - 1
        while i>=0:
            if s[i] == 'V':
                if i > 0 and s[i-1] == 'I':
                    number += 4
                    i -= 1
                else:
                    number += 5
            elif s[i] == 'X':
                if i > 0 and s[i-1] == 'I':
                    number += 9
                    i -= 1
                else:
                    number += 10
            elif s[i] == 'L':
                if i > 0 and s[i-1] == 'X':
                    number += 40
                    i -= 1
                else: 
                    number += 50
            elif s[i] == 'C':
                if i > 0 and s[i-1] == 'X':
                    number += 90
                    i -= 1
                else:
                    number += 100
            elif s[i] == 'D':
                if i > 0 and s[i-1] == 'C':
                    number += 400
                    i -= 1
                else:
                    number += 500
            elif s[i] == 'M':
                if i > 0 and s[i-1] == 'C':
                    number += 900
                    i -= 1
                else:
                    number += 1000
            else:
                number += 1
            i -= 1
        return number
            
            
                


            

        
        