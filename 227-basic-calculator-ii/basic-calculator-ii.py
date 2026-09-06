class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        pre_op = '+'
        s+='+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                    pass
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    e = stack.pop()
                    stack.append((e*num))
                elif pre_op == '/':
                    e = stack.pop()
                    stack.append(int(e / num))
                num = 0
                pre_op = c
        return sum(stack)