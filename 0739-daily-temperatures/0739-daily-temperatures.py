class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono_stack = []

        for i in range(len(temperatures)):
            # we compare the temperature at the top of the stack with the next greatest temp we found
            while mono_stack and temperatures[i]>temperatures[mono_stack[-1]]:
                value_popped = mono_stack.pop()
                res[value_popped] = i - value_popped
            # if stack is empty or the next temp is lesser than the top of the stack
            mono_stack.append(i)
        #for days where they will not have next higher temp
        while mono_stack:
            res[mono_stack.pop()] = 0
        return res
        