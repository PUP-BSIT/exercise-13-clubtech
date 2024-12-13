def menu():
    while True:
        print("---------------------------------------------")
        print("Greetings, John Matthew")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comments from teammates")
        print("4. Exit")
        print("----------------------------------------------")
        user_input = int(input("Choose your option: "))

        match user_input:
            case 1:
                basic_info()
            case 2:
                goals()
            case 3:
                comments()
            case 4:
                break

def basic_info():
    print("Age: 19")
    print("Birthday: January 1, 2005")
    print("Location: Pasay City")
    print("Hobbies: Cycling, reading, playing pc games")
    print("Favorite Food: Chicken Curry and bonding with pizza")
    print("Favorite Anime: One Piece")

def goals():
    print("My goals are: ")
    print("-graduate college and become a good programmer by developing my IT"
          " skills develop myself physically and spiritually through"
          " exercise and bible reading")
    
def comments():
    print("This code has been reviewed by Franco Alfonso Lazaro")
    print("Greetings from John Carlo I. Nolluda")

menu()
