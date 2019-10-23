def obtain_grade():
    mark = None

    grade_lookup = {
        
    }

    while mark is None:
        try:
            mark = float(input("Enter mark: "))

            if not 0 <= mark <= 100:
                mark = None

        except TypeError:
            continue

    if mark <