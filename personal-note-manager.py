print("==== Prsonal Notes Manager ====")

while True:
    print("\n1.Add Note")
    print("2.View Notes")
    print("3.Exit")

    choice=input("Enter choice:")

    if choice=="1":
        note=input("Enter your note:")

        with open("notes.txt","a")as file:
            file.write(note+"\n")
            print("Not saved!")

    elif choice=="2":
        try:
            with open("notes.txt","r")as file:
                print("\n your notes:")
                print(file.read())
        except FileNotFoundError:
            print("no notes found!")

    elif choice=="3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")