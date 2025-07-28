class Logger:

    def __init__(self):
        self.message_to_timestamp_map = dict()
        
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.message_to_timestamp_map:
            previous_timestamp = self.message_to_timestamp_map[message]
            if timestamp - previous_timestamp < 10:
                return False
            else:
                self.message_to_timestamp_map[message] = timestamp
                return True
        else:
            self.message_to_timestamp_map[message] = timestamp
            return True
        

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)