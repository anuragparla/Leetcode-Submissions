class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        trigger: next warmer aka next greater
        '''
        '''
        pattern: monotonic decreasing stack
        '''
        answer = [0] * len(temperatures)
        mon_dec_stack = []
        for i, curr in enumerate(temperatures):

            while mon_dec_stack and mon_dec_stack[-1][0] < curr:
                tmp,idx = mon_dec_stack.pop()
                answer[idx] = i - idx
            mon_dec_stack.append((curr,i))
        return answer



        