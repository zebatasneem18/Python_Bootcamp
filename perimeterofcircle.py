import math

def calculate_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter

def main():
    radius = float(input("Enter the radius of the circle: "))
    perimeter = calculate_perimeter(radius)
    print(f"The perimeter of the circle with radius {radius} is: {perimeter:.2f}")

if __name__ == "__main__":
    main()
