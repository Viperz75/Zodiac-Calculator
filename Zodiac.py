#Zodiac Sign

def month():
    print("1 - January")
    print("2 - Febuary")
    print("3 - March")
    print("4 - April")
    print("5 - May")
    print("6 - June")
    print("7 - Jully")
    print("8 - August")
    print("9 - September")
    print("10 - October")
    print("11 - Novemver")
    print("12 - December")
month()

def zodiac():
    month = input("Month of birth:")
    day = int(input("Day of birth:"))
    birth_day = ( month + "/" + str(day))
    if (int(month) > 12):
        month()
        zodiac()
    elif month == "1":
        if (day > 31):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 20):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Capricorn!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Aquarius!")
    elif month == "2":
        if (day > 28):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 18):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Aquarius!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Pisces!")
    elif month == "3":
        if (day > 31):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 20):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Pisces!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Aries!")
    elif month == "4":
        if (day > 30):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 20):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Aries!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Taurus!")
    elif month == "5":
        if (day > 31):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 20):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Taurus!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Gemini!")
    elif month == "6":
        if (day > 30):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 21):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Gemini!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Cancer!")
    elif month == "7":
        if (day > 31):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 22):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Cancer!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Leo!")
    elif month == "8":
        if (day > 31):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 23):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Leo!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Virgo!")
    elif month == "9":
        if (day > 30):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 23):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Virgo!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Libra!")
    elif month == "10":
        if (day > 31):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 23):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Libra!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Scorpio!")
    elif month == "11":
        if (day > 30):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 23):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Scorpio!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Sagittarius!")
    elif month == "12":
        if (day > 31):
            print("Invalid Date")
            print("Please try again!")
            zodiac()
        elif (day <= 21):
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Sagittarius!")
        else:
            print("Your Birthday is(mm/dd):", birth_day)
            print("Then your zodiac sign is Capricorn!")
zodiac()