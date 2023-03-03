import module

#main fuction
while True:
    print("------------------------------")
    print("| AIUB LAB Management System |")
    print("------------------------------")
    print("|     1. Add PC              |")
    print("|     2. Update PC           |")
    print("|     3. Remove PC           |")
    print("|     4. Display all PCs     |")
    print("|     5. Check specific PC   |")
    print("|     6. Search PC           |")
    print("|     7. Store PCs           |")
    print("------------------------------")
    print("|         0. Quit            |")
    print("------------------------------")
    choice = input("Enter your choice (1-7), or '0' to quit: ")
    print("\033[A                             \033[A")
    print("\033[A                             \033[A")
    if choice == "1":
        module.add_pc()
    elif choice == "2":
        pc_num = input("Enter PC number to update: ")
        module.update_pc(pc_num)
        print("\033[A                             \033[A")
        print("\033[A                             \033[A")
    elif choice == "3":
        pc_num = input("Enter PC number to remove: ")
        module.remove_pc(pc_num)
        print("\033[A                             \033[A")
        print("\033[A                             \033[A")
    elif choice == "4":
        module.display_all_pcs()
        print("\033[A                             \033[A")
        print("\033[A                             \033[A")
    elif choice == "5":
        pc_num = input("Enter PC number to display: ")
        module.display_pc(pc_num)
        print("\033[A                             \033[A")
        print("\033[A                             \033[A")
    elif choice == "6":
        module.search_pc()
        print("\033[A                             \033[A")
        print("\033[A                             \033[A")
    elif choice == "7":
        module.store_pcs()
        print("\033[A                             \033[A")
        print("\033[A                             \033[A")
    elif choice == "0":
        print("Thanks for using our system! :D")
        break
    else:
        print("Invalid choice.")