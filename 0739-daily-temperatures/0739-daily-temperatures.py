class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        mono_stack = []

        for i in range(len(temperatures)):
            while mono_stack and temperatures[i]>temperatures[mono_stack[-1]]:
                idx = mono_stack.pop()
                days = i - idx
                result[idx] = days
            mono_stack.append(i)
        return result
        