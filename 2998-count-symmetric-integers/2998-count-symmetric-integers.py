import math
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        '''
        low 
        high 
        if x has 2*n digits will be symm if sum of first n digits of x == sum of last n digits of x
        if there are odd number of digits then this is not symmetric 
        11 | no of digits = 2 => 2 //2 = 1 => 2 *1 
        1203 | no of digits = 4 => 4//2 = 2 => 1+2 = 0+3 
        '''
        '''
        visit every number in the range 
        need to count total number of digits 
        store the digits in a list 
        find the value of n by using above formula 
        now if the len of list is odd then return 0 
        else count of digits that are symmetric 
        '''
        count = 0 

        for i in range(low,high+1):
            store_digits = []
            num = i 

            while num>0:
                digit = num % 10
                store_digits.insert(0, digit)
                num//=10
        
            n = len(store_digits)//2
            first_n = store_digits[:n]
            last_n = store_digits[-n:]

            if len(store_digits) % 2 == 0:
                sum_first_n = sum(first_n)
                sum_last_n = sum(last_n)
                if sum_first_n == sum_last_n:
                    count+=1 
        return count
            
                
            
            
