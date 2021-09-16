def calculateArea():
    base = float(input("Enter your base value: "))
    height = float(input("Enter the height value: "))

    area = 0.5 * base * height

    return area

result = calculateArea()

print(result)