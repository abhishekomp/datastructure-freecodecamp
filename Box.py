class Box:
  def __init__(self, length, breadth):
    print("Box parameterized Construtor invoked")
    self.length = length
    self.breadth = breadth

  def __str__(self):
    print(f"str dunder method invoked")
    return f"Box length->{self.length}, breadth->{self.breadth}"
  
  def __len__(self):
    return self.length
  
  # Even though this method is defined to be visually like a dunder method, invoking it similar to len(self) does not work i.e. i cannot invoke this dunder method from another method.
  # Neither can I invoke this method from outside the class to get the breadth of the box but the same is possible for the __len__ dunder method
  def __breadth__(self):
    return self.breadth
  
  def getArea(self):
    return self.length * self.breadth
  
  # Getting length using a dunder method. Using a dunder method in another method works fine for len
  def getLengthByInvokingDunderMethod(self):
    return len(self)

  # Getting length from the instance variable
  def getLength(self):
    return self.length

  # Getting length from the instance variable
  def getBreadth(self):
    return self.breadth

  def calculateArea(self):
    return self.getLength() * self.getBreadth()
  
  # Invoking dunder method to get the breadth does not work but it works to get the length using len dunder method
  # def getAreaUsingDunder(self):
  #   return len(self) * breadth(self)
  
  def incrementLengthAndGetArea(self, extraLength):
    self.length += extraLength
    return self.getArea()

# Usage of the Box class and dunder method
box = Box(10, 5)
print(f"Area: {box.getArea()}")
print(f"Area using calculate area: {box.calculateArea()}")
print(f"Box Dimensions: {box.length}, {box.breadth}")
print(box)
print(f"Area after length increment: {box.incrementLengthAndGetArea(10)}")
print(f"Box Dimensions: {box.length}, {box.breadth}")
print(f"Box Dimensions using method inovocation: {box.getLength()}, {box.getBreadth()}")
print(f"Length: {len(box)}")
print(f"Length: {box.getLengthByInvokingDunderMethod()}")

# NameError: name 'breadth' is not defined. Cannot invoke this dunder method.
# print(f"Length: {breadth(box)}")