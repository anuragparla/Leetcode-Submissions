import collections
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 0 or nums is None or len(nums) == 1:
            return True
        destination = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >=destination:
                destination = i
        if destination == 0:
            return True
        return False

    #     self.visited = set()
    #     return self.dfs(0,nums)

    # def dfs(self,root, nums):
    #     if root == len(nums)-1:
    #         return True
    #     if root in self.visited:
    #         return False
    #     self.visited.add(root)
    #     for i in range(1,nums[root]+1):
    #         child = root + i 
    #         if(self.dfs(child, nums)):
    #             return True

    #     return False

        # queue = collections.deque([0])
        # visited.add(0)
        # n = len(nums)
        # while queue:
        #     currNode = queue.popleft()
        #     for i in range(1, nums[currNode]+1):
        #         child = currNode + i
        #         if currNode == n - 1:
        #             return True
        #         if child not in visited:
        #             queue.append(child)
        #             visited.add(child)
        
        # return False 
        

                    
        