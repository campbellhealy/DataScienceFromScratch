# classes.py

class CountingClicks():
    """Doc Statement"""
    def __init__(self, count = 0):
        self.count = count

    def __repr__(self):
        return f'CountingClicks(count={self.count}'

    def click(self, num_times = 1):
        """Clicks of the Clicker to count"""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


class NoResetClicks():
    """Doc Statement"""
    def __init__(self, count = 0):
        self.count = count

    def __repr__(self):
        return f'CountingClicks(count={self.count}'

    def click(self, num_times = 1):
        """Clicks of the Clicker to count"""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        pass