import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Min heap solution
        '''
        if len(nums) == 0 or nums is None:
            return -1 
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq,nums[i])
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]
        