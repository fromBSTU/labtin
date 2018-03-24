class Litera:
    """Symbol of alphabet with its probability
       Addition: for huffman coding"""
    def __init__(self, ltr, probability):
        self.__ltr = ltr
        if probability <= 1 and probability >= 0:
            self.__probability = probability
        else:
            self.__probability = 0
        self.__lson = None
        self.__rson = None
        self.__parent = None
        self.__code = 'c'
    def setltr(self, ltr):
        self.__ltr = ltr
    def setprob(self, probability):
        if probability <= 1 and probability >= 0:
            self.__probability = probability
        else:
            self.__probability = 0
    def getltr(self):
        return self.__ltr
    def getprob(self):
        return self.__probability
    def printlitera(self):
        print("(", self.__ltr, ",", self.__probability, ")", end = '')
    def __lt__(self, other):
        return self.__probability < other.__probability
    def __gt__(self, other):
        return self.__probability > other.__probability
    def __le__(self, other):
        return self.__probability <= other.__probability
    def __ge__(self, other):
        return self.__probability >= other.__probability
    def __ne__(self, other):
        return self.__probability != other.__probability
    #for huffman coding
    def parent(self, other):
        parent = Litera("0", 0)
        parent.__probability = self.__probability + other.__probability
        parent.__ltr = self.__ltr + other.__ltr
        parent.__lson = self
        parent.__rson = other
        self.__parent = parent
        other.__parent = parent
        self.__code = "0"
        other.__code = "1"
        return parent
    def getlson(self):
        return self.__lson
    def getrson(self):
        return self.__rson
    def getparent(self):
        return self.__parent
    def union(self):
        """sons code = sons code + code of parent
           self is parent"""
        if self.__lson is None and self.__rson is None:
            return
        self.__lson.__code = self.__code + self.__lson.__code
        self.__rson.__code = self.__code + self.__rson.__code
    def print_with_code(self):
        print("(", self.__ltr, ", ", self.__probability, ", ", self.__code, ")", end='')

