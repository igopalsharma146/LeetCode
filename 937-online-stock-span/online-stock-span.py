class StockSpanner:

    def __init__(self):
        self.stack1=[]

    def next(self, price: int) -> int:
        current_price,current_value=price,1
        stack=self.stack1
        while stack and stack[-1][0] <= current_price:
            prev_price,prev_value=stack.pop()
            current_value+=prev_value
        stack.append((current_price,current_value))
        return current_value


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)