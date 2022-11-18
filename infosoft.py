
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.map and self.map[message] > timestamp - 5:
            return False
        
        # reset the time
        self.map[message] = timestamp
        return True

#Your Logger object will be instantiated and called as such:
obj = Logger()
param_1 = obj.shouldPrintMessage(timestamp=0,message="hello")
param_2 = obj.shouldPrintMessage(timestamp=1,message="word")
param_3 = obj.shouldPrintMessage(timestamp=6,message="hello")
param_4 = obj.shouldPrintMessage(timestamp=7,message="hello")
param_5 = obj.shouldPrintMessage(timestamp=8,message="word")
print(param_1)
print(param_2)
print(param_3)
print(param_4)
print(param_5)


