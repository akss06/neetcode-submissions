class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        

        for i in range(len(operations)):
            ch = operations[i].lstrip("-")
            if ch.isnumeric():
                stack.append(operations[i])
                print(stack)

            elif operations[i] == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))
                print(stack)

            elif operations[i] == "D":
                stack.append(2 * int(stack[-1]))
                print(stack)

            else:
                stack.pop()
                print(stack)

        print(stack)

        s = 0

        for i in stack:
            s = s + int(i)

        return s
        

        

            
        