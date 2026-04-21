def circle_area():
    while True:
        Pi = float(3.1415926535)
        Radius = input("Enter the radius of the circle: " )
        try:
            Radius = float(Radius)
            Area = Pi*Radius**2
            print (f"Area of the Circle is {Area}.")
            break
        except ValueError:
            print("Enter a numerical value for the code to work")
    
def rectangle_area():
    while True:
        Length = input("Enter length of rectangle: ")
        Width = input("Enter the width of rectangle: " )
        try:
            Length = float(Length)
            Width = float(Width)
            Area =Length*Width
            print(f"Area of the Rectangle is {Area}.")
            break
        except ValueError:
            print("Enter a numerical value for the code to work")

def triangle_area():
    while True:
        Base = input("Enter base ot triangle: ")
        Height = input("Enter height of triangle: ")
        try:
            Base = float(Base)
            Height= float(Height)
            Area = 0.5*Base*Height
            print(f"Area of the Triangle is {Area}.")
            break
        except ValueError:
            print("Enter a numerical value for the code to work")

def selection_area():
    while True:
        select = input("What area do you want to calculate,Circle,Rectangle,Triangle press Exit if none.: ").lower().strip()
        if select == "rectangle":
            rectangle_area()
        elif select == "triangle":
            triangle_area()
        elif select == "circle":
            circle_area()
        elif select == "exit":
            break
        else: 
            print("Invalid choices enter Rectangle,Circle or Triangle")

selection_area()