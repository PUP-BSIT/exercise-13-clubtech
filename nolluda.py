def nolluda_menu():
    user_input = 0
    while user_input != 4:
        print("==============================")
        print("Greetings! John Carlo I. Nolluda")
        print("1. Basic info")
        print("2. Goals")
        print("3. Comments from teammates")
        print("4. Exit")
        print("==============================")
        user_input = int(input("Enter your option: "))

        if user_input == 1:
            print("===============================================================")
            print("Age: 20")
            print("Birthday: September 18, 2004")
            print("Location: Guiho St. Creekland Hagonoy, Taguig City")
            print("Hobbies: Ml, Cycling, Playing lol")
            print("Favorite foods: Bicol express, sinigang na baboy, adobong baboy ")
            print("================================================================")

        elif user_input == 2:
            print("=================")
            print("My goals are: ")
            print("finish college")
            print("buy bike/motor")
            print("=================")
    
        elif user_input == 3:
            print("This code has been reviewed by Franco Alfonso Lazaro ")
            print("This code has been reviewed by John Matthew Arroyo") 
