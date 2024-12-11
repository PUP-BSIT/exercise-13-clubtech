def lazaro_menu():
    user_input = 0    
    while user_input != 4:
        print("=======================================")
        print("Greetings: Franco Alfonso C. Lazaro")
        print("1-Basic Info")
        print("2-Goals ")
        print("3-Comments from teammates")
        print("4-Exit")
        print("=======================================")
        user_input =  int(input("Enter your choice: "))

        if user_input == 1:
            print("=====================================================")
            print("Age: 19")
            print("Birthday: April 11, 2005")
            print("Hobby: Watching anime, reading manga, drawing")
            print("Favorite Food: Okonomiyaki")
            print("Favorite car: Citroen 2cv, Fiat nuova 500")
            print("Favorite Anime: Lupin III, Assassination Classroom")
            print("=====================================================") 
    
        elif user_input == 2:
            print("=============== Goals ==============") 
            print("To become an artist or game developer")
            print("Create my own animated series")
            print("To become a great animator")
            print("=====================================")
    
        elif user_input == 3:
        #teammates comments
            print("This code has been reviewed by John Carlo Nolluda")
            print("This code has been reviewed by John Matthew Arroyo")

        else:
            pass 
        