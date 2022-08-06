age = input("How old are you?")

if age == '':
    print("No age, no entry.")
else:
    age = int(age)
    if age < 18:
        print("Sorry kiddo, try again next year.")
    elif age >= 18 and age <= 20:
        print("Enjoy the show, but stay off the goofy juice.")
    else:
        print("Party on, Garth!")