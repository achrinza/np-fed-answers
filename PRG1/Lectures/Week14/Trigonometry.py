import math

def main() -> None:
    print("{:<8} {:<8} {:<8} {:<8}".format("Degree", "Radians", "Sin", "Cos"))

    for i in range(0, 361, 10):
        print("{:10d} {:<8.2f} {:<8.2f} {:<8.2f}".format(i, math.degrees(i), math.radians(i), math.sin(i), math.cos(i)))

if __name__ == "__main__":
    main()