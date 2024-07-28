import math

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle with radius {radius} is: {area:.2f}")

if __name__ == "__main__":
    main()
