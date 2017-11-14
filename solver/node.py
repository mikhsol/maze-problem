class Node(object):
    def __init__(self, value=None, row=None, col=None, prev=None):
        self.value = value
        self.row = row
        self.col = col
        self.prev = prev

    def __eq__(self, other):
        return self.value == other.value \
               and self.row == other.row \
               and self.col == other.col \
               and self.prev == other.prev
