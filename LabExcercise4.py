import os  

doc_path = os.path.expanduser("~/Documents")


if not os.path.exists(doc_path):
    os.makedirs(doc_path)

def register_student():
    print("\n--- Register Student ---")
    student_no = input("Student No.: ")
    last_name = input("Last Name: ")
    first_name = input("First Name: ")
    middle_initial = input("Middle Initial: ")
    program = input("Program: ")
    age = input("Age: ")
    gender = input("Gender: ")
    birthday = input("Birthday: ")
    contact_no = input("Contact No.: ")

    
    data = [
        f"Student No.: {student_no}",
        f"Full Name: {last_name}, {first_name} {middle_initial}.",
        f"Program: {program}",
        f"Age: {age}",
        f"Gender: {gender}",
        f"Birthday: {birthday}",
        f"Contact No.: {contact_no}"
    ]

    file_path = os.path.join(doc_path, student_no + ".txt")

    try:
        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")
        print(" Student registered successfully!\n")
    except Exception as e:
        print(f" Error saving student record: {e}\n")

def open_student_record():
    print("\n--- Open Student Record ---")
    student_no = input("Enter Student No.: ")
    file_path = os.path.join(doc_path, student_no + ".txt")

    try:
        with open(file_path, "r") as f:
            print("\n Student Record:")
            for line in f:
                print(line.strip())
            print()
    except FileNotFoundError:
        print(" Student record not found.\n")

def main_menu():
    while True:
        print("==== Student Records Management ====")
        print("1. Register Student")
        print("2. Open Student Record")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            open_student_record()
        elif choice == "3":
            print("\n Goodbye! Thank you for using the system.")
            break
        else:
            print(" Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
