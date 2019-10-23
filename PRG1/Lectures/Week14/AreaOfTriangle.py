import math

def main():
    def is_valid(side_a, side_b, side_c):
        return side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b

    def find_area(side_a, side_b, side_c) -> float:
        s = (side_a + side_b + side_c ) / 2
        area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
        return area

    side_a = int(input("Enter length of Side A: "))
    side_b = int(input("Enter length of Side B: "))
    side_c = int(input("Enter length of Side C: "))

    if is_valid(side_a, side_b, side_c):
        print("Input lengths can form a triangle of area {:.2f} square units".format(find_area(side_a, side_b, side_c)))
    else:
        print("Input lengths cannot form a triangle.")


if __name__ == "__main__":
    main()