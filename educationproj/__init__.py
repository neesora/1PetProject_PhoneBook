def check_triangle(side1, side2, side3):

    if side1 == side2 == side3:
        print('Triangle is equalateral')
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print('Triangle is isosceles')
    else:
        print('Triangle is scalene')
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
check_triangle(side1, side2, side3)