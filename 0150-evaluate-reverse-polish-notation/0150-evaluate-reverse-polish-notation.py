class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polish_notation_Stack = []
        result = 0

        for i in range(len(tokens)):

            if tokens[i] == '+':
                if len(polish_notation_Stack)>1:
                    result = int(polish_notation_Stack[-2]) + int(polish_notation_Stack [-1])
                    polish_notation_Stack.pop()
                    polish_notation_Stack.pop()
                    polish_notation_Stack.append(result)
            elif tokens[i] == '-':
                if len(polish_notation_Stack)>1:
                    result = int(polish_notation_Stack[-2]) - int(polish_notation_Stack [-1])
                    polish_notation_Stack.pop()
                    polish_notation_Stack.pop()
                    polish_notation_Stack.append(result)
            elif tokens[i] == '*':
                if len(polish_notation_Stack)>1:
                    result = int(polish_notation_Stack[-2]) * int(polish_notation_Stack [-1])
                    polish_notation_Stack.pop()
                    polish_notation_Stack.pop()
                    polish_notation_Stack.append(result)
            elif  tokens[i] == '/':
                if len(polish_notation_Stack)>1:
                    result = int(polish_notation_Stack[-2]) / int(polish_notation_Stack [-1])
                    polish_notation_Stack.pop()
                    polish_notation_Stack.pop()
                    polish_notation_Stack.append(result)
            else:
                polish_notation_Stack.append(tokens[i])
            
        if len(polish_notation_Stack) != 0 :
            return int(polish_notation_Stack[-1])

                
        