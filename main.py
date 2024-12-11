import arroyo, lazaro, nolluda 
main_input = 0
while main_input != 4:
    print("--------------------")
    print("CLUBTECH Members: ")
    print("1. John Matthew S. Arroyo")
    print("2. Franco Alfonso C. Lazaro")
    print("3. John Carlo I. Nolluda")
    print("4. Exit")
    print("--------------------")
    main_input = int(input("Enter member choice: "))

    if main_input == 1:
        arroyo.arroyo_menu()

    elif main_input == 2:
        lazaro.lazaro_menu()

    elif main_input == 3:
        nolluda.nolluda_menu()

    else:
        pass

    
