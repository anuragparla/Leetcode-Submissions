# using 2 pointers
#Time complexity is O(N) and space is O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) -1;
        res = []

        for i in range(len(numbers)):

            if p1 != p2:

                if numbers[p1] + numbers[p2] == target:
                    res.append(p1+1)
                    res.append(p2+1)
                    break
                elif numbers[p1] + numbers[p2] > target:

                    p2 -=1
                elif numbers[p1] + numbers[p2] < target:

                    p1 +=1
        return res
