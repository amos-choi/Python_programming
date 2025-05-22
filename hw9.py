class Point:
    def __init__(self, x1 = 0, y1 = 0):
        self.__x1 = x1
        self.__y1 = y1
        
    def set(self, x1, y1):
        self.__x1 = x1
        self.__y1 = y1

    def get(self):
        return (self.__x1, self.__y1)

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)
    
    def show(self):
        print(f'좌측 상단 꼭짓점이  {self.lt.get()[0], self.lt.get()[1]}이고 우측 하단 꼭지점이 {self.rb.get()[0], self.rb.get()[1]}인 사각형입니다')
        
    def getWidth(self):
        return self.rb.get()[0] - self.lt.get()[0]
                
    def getHeight(self):
        return self.rb.get()[1] - self.lt.get()[1]
        
    def getArea(self):
        width = self.getWidth()
        height = self.getHeight()
        area = width * height
        return area
        
    def getPerimeter(self):
        width = self.getWidth()
        height = self.getHeight()
        return width * 2 + height * 2
        
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는  {a}, 둘레는  {p}')
