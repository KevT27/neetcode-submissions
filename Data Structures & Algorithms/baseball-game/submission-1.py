class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        total = 0

        for n in operations:

            if n == "+":
                temp = stack[-1] + stack[-2]
                stack.append(temp)

            elif n == "D":
                stack.append(stack[-1] * 2)

            elif n == "C":
                stack.pop()

            else:
                stack.append(int(n))
            
        for num in stack:
            total += num

        return total
