print("Conversion ( Units of length ) ")
def Options():
    print('''    [01] Miles - Kilometre
    [02] Miles - Metre
    [03] Miles - Centimetre
    [04] Miles - Millimetre
    [05] Kilometre - Miles
    [06] Kilometer - Metre
    [07] Kilometre - Centimetre
    [08] Kilometre - Millimetre
    [09] Metre - Miles
    [10] Meter - Kilometre
    [11] Metre - Centimetre
    [12] Metre - Millimetre
    [13] Centimetre - Miles
    [14] Centimetre - Kilometre
    [15] Centimetre - Metre
    [16] Centimetre - Millimetre
    [17] Millimetre - Miles
    [18] Millimetre - Kilometre
    [19] Millimetre - Metre
    [20] Millimetre - Centimetre
    [21] Exit''')
    Opt = input("Choose an option ( Enter a number ): ")
    # miles
    if Opt == "1":
        print("Miles - Kilometre")
        num = input("Number of miles: ")
        km = float(num) * 1.60934
        print(f'{num} mile(s) in kilometre(s) is {km}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "2":
        print("Miles - Metre")
        num = input("Number of miles: ")
        m = float(num) * 1609.34
        print(f'{num} mile(s) in metre(s) is {m}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "3":
        print("Miles - Centimetre")
        num = input("Number of miles: ")
        cm = float(num) * 160934
        print(f'{num} mile(s) in centimetre(s) is {cm}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "4":
        print("Miles - Millimetre")
        num = input("Number of miles: ")
        mm = float(num) * 160934
        print(f'{num} mile(s) in millimetre(s) is {mm}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    # kilometres
    elif Opt == "5":
        print("Kilometre - Miles")
        num = input("Number of kilometres: ")
        mi = float(num) / 1.60934
        print(f'{num} kilometre(s) in mile(s) is {mi}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "6":
        print("Kilometer - Metre")
        num = input("Number of kilometres: ")
        m = float(num) * 1000
        print(f'{num} kilometre(s) in metre(s) is {m}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "7":
        print("Kilometre - Centimetre")
        num = input("Number of kilometres: ")
        cm = float(num) * 100000
        print(f'{num} kilometre(s) in centimetre(s) is {cm}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "8":
        print("Kilometre - Millimetre")
        num = input("Number of kilometres: ")
        mm = float(num) * 1000000
        print(f'{num} kilometre(s) in millimetre(s) is {mm}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    # metres
    elif Opt == "9":
        print("Metre - Miles")
        num = input("Number of metres: ")
        mi = float(num) / 1609.34
        print(f'{num} metre(s) in mile(s) is {mi}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "10":
        print("Meter - Kilometre")
        num = input("Number of metres: ")
        km = float(num) / 1000
        print(f'{num} metre(s) in kilometre(s) is {km}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "11":
        print("Metre - Centimetre")
        num = input("Number of metres: ")
        cm = float(num) * 100
        print(f'{num} metre(s) in centimetre(s) is {cm}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "12":
        print("Metre - Millimetre")
        num = input("Number of metres: ")
        mm = float(num) * 1000
        print(f'{num} metre(s) in millimetre(s) is {mm}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    # centimetres
    elif Opt == "13":
        print("Centimetre - Miles")
        num = input("Number of centimetres: ")
        mi = float(num) / 160934
        print(f'{num} centimetre(s) in mile(s) is {mi}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "14":
        print("Centimetre - Kilometre")
        num = input("Number of centimetres: ")
        km = float(num) / 100000
        print(f'{num} centimetre(s) in centimetre(s) is {km}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "15":
        print("Centimetre - Metre")
        num = input("Number of centimetres: ")
        m = float(num) / 100
        print(f'{num} centimetre(s) in metre(s) is {m}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "16":
        print("Centimetre - Millimetre")
        num = input("Number of centimetres: ")
        mm = float(num) / 10
        print(f'{num} centimetre(s) in millimetre(s) is {mm}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    # millimetres
    elif Opt == "17":
        print("Millimetre - Miles")
        num = input("Number of millimetres: ")
        mi = float(num) / 1609347.0878864445
        print(f'{num} millimetre(s) in mile(s) is {mi}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "18":
        print("Millimetre - Kilometre")
        num = input("Number of millimetres: ")
        km = float(num) / 1000000
        print(f'{num} millimetre(s) in kilometre(s) is {km}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "19":
        print("Millimetre - Metre")
        num = input("Number of millimetres: ")
        m = float(num) / 1000
        print(f'{num} millimetre(s) in metre(s) is {m}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)

    elif Opt == "20":
        print("Millimetre - Centimetre")
        num = input("Number of millimetres: ")
        cm = float(num) / 10
        print(f'{num} millimetre(s) in centimetre(s) is {cm}')
        Opt2 = input("Do you want to continue ( Y/n )? ")
        Opt2.lower()
        if Opt2 == "y":
            Options()

        elif Opt2 == "n":
            exit(0)
    elif Opt == "21":
        exit(0)
    else:
        print("Please enter a number from 1-21")


Options()
