class Base:
    def __init__(self, x, y):  # constructor for Base class
        #self indicates that those variables are of that class
        self.x = x
        self.y = y

class Circle(Base):
    def __init__(self, x, y, size):  # constructor for Circle class
        super().__init__(x, y)   # calls constructor in superclass to assignvalues to self.x and self.y
        self.size = size

    def shape(self):
        return "This is a circle"

    def draw(self):
        return f"""
        ({self.x}, {self.y})
        {self.size}
             , - ~ ~ ~ - ,
         , '               ' ,
       ,                       ,
      ,                         ,
     ,                           ,
     ,                           ,
     ,                           ,
      ,                         ,
       ,                       ,
         ,                  , '
           ' - , _ _ _ ,  '
    """
