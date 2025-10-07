import os

doc_path = os.path.expanduser("Documents")

if not os.path.exists(doc_path):
    os.makedirs(doc_path)

while True:
    print("\n Student Registration System")
    print("1. Register Student")
    print("2. View Student Record")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        print("\n--- Student Registration ---")
        student_no = input("Enter Student Number: ") 
        last_name = input("Enter Last Name: ")
        first_name = input("Enter First Name: ")
        program = input("Enter Program: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        birthdate = input("Enter Birthdate (YYYY-MM-DD): ")
        contact_no = input("Enter Contact Number: ")

        data = [
            f"Student Number: {student_no}",
            f"Last Name: {last_name}",
            f"First Name: {first_name}",
            f"Program: {program}",
            f"Age: {age}", 
            f"Gender: {gender}",
            f"Birthdate: {birthdate}",
            f"Contact Number: {contact_no}"
        ]

        file_path = os.path.join(doc_path, f"student_{student_no}.txt")
   
        with open(file_path, "w") as file:
            for line in data:
                file.write(line + "\n")

        print(f"\n Student record saved to {file_path}")

    elif choice == "2":
        print("\n--- View Student Record ---")
        student_no = input("Enter Student Number: ")
        file_path = os.path.join(doc_path, f"student_{student_no}.txt") 

        try:
            with open(file_path, "r") as file:
                print("\n Student Records:")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(f"No records found for Student Number: {student_no}")

    elif choice == "3":
        print("\nExiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
