class Solution:
    def calculate(self, s: str) -> int:
        value = 0 
        sign = '+'
        stack_of_values = []

        for i,c in enumerate(s):
            if c.isdigit():
                value = value * 10 + int(c)
            if i == len(s) - 1 or c in '+-*/':
                if sign == '+':
                    stack_of_values.append(value)
                if sign == '-':
                    stack_of_values.append(-value)
                if sign == '*':
                    stack_of_values.append(stack_of_values.pop() * value)
                if sign == '/': 
                    stack_of_values.append(int( stack_of_values.pop() /value))
                sign = c
                value = 0
        return sum(stack_of_values)