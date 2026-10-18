print("==== Prsonal Notes Manager ====")

while True:
    print("\n1.Add Note")
    print("2.View Notes")
    print("3. Search Notes")
    print("4. Delete Notes")
    print("5.Exit")

    choice=input("Enter choice:")

    try:
        with open("notes.txt","r") as file:
            notes=file.readlines()
    except FileNotFoundError:
        notes=[]

    if choice=="1":
        note=input("Enter your note:")

        with open("notes.txt","a")as file:
            file.write(note+"\n")
            print("Note saved!")

    elif choice=="2":
        try:
            with open("notes.txt","r")as file:
                print("\n your notes:")
                print(file.read())
        except FileNotFoundError:
            print("no notes found!")

    elif choice=="3":
        keyword=input("Enter keyword:").lower()
        found=False

        for note in notes:
            if keyword in note.lower():
                print(note.strip())
                found=True

        if not found:
            print("No matching notes!")


    elif choice=="4":
        if not notes:
            print("No notes to delete!")
            continue
        for i,note in enumerate(notes,1):
            print(i,note.strip())

        try:
            number=int(input("Enter note number to delete:"))
            if 1<=number<=len(notes):
                notes.pop(number-1)
                with open("notes.txt","w") as file:
                    file.writelines(notes)
                    print("note deleted!")

            else:
                print("Invalid note number!")

        except ValueError:
            print("Enter a vallid number!")


    elif choice=="5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")