def main():
    p01 = [86, 80, 75, 82, 80, 70]
    p02 = [40, 55, 60, 48, 50]
    p03 = [90, 85, 30, 86, 78, 75, 54]

    marks_list = [p01, p02, p03]

    print("{:<8} {:<8}".format("Class", "Average"))
    for i, phys_class in enumerate(marks_list):
        print("{:<8} {:<8}".format("P0" + str(i + 1), sum(phys_class)/len(phys_class)))


if __name__ == "__main__":
    main()