class MyCalendar(object):

    def __init__(self):
        self.lis1 = []
    
    def book(self, start, end):
        if (end<=start):
            return False
        
        i = bisect.bisect_right(self.lis1,start)
        if i%2:
            return False
        
        j = bisect.bisect_left(self.lis1,end)
        if i!=j:
            return False
        self.lis1[i:i] = [start,end]
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
