class ProductOfNumbers(object):

    def __init__(self):
        # Initialize with 1 to handle multiplication smoothly
        self.prefix = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            # Reset prefix products because any future product including this 0 is 0
            self.prefix = [1]
        else:
            # Append the new running product
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        # If k >= len(self.prefix), a zero was added within the last k numbers
        if k >= len(self.prefix):
            return 0
        
        # Use // for integer division so it works in both Python 2 and Python 3
        return self.prefix[-1] // self.prefix[-1 - k]
