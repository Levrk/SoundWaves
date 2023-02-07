class linespace():
    def __init__(self,linespace):
        """
        initializizes linespace object
        self.x : list of x values
        self.y : list of y values
        """
        self.x = linespace[0]
        self.y = linespace[1]
    
    def __add__(self, other):
        #overriding + operator
        self.y = [y1 + y2 for y1, y2 in zip(self.y, other.y)]
        return self
    
    def __mul__(self,other):
        #overriding * operator
        self.y = [y1 * y2 for y1, y2 in zip(self.y, other.y)]
        return self

    def __sub__(self,other):
        #overriding - operator
        self.y = [y1 - y2 for y1, y2 in zip(self.y, other.y)]
        return self

    def __div__(self,other):
        #overriding / operator
        self.y = [y1 / y2 for y1, y2 in zip(self.y, other.y)]
        return self

    def get_max(self):
        return max(self.y)
    

