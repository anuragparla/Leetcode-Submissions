this is a greedy problem 
sorting the list and applying two pointers is the approach 
time complexity: O(n log n)
space complexity: O(n) for python since Tim sort uses combination of merge & insert
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lp, rp = 0, len(people)-1
        boat = 0
        while lp<=rp:
            if people[lp] + people[rp] <=limit:
                lp +=1 
            rp -=1
            boat +=1 
        return boat
