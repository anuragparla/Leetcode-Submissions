class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])
        sum = 0
        max = 0
        for i in range(0,m):
            for j in range(0,n):
                sum = sum+accounts[i][j]
            if sum>max:
                max = sum
            sum = 0
        return max
                
        