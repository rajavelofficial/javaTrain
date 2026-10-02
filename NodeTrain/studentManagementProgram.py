def main():
    students = {}  # Dictionary to store student name and marks

    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. Display students")
        print("3. Search student")
        print("4. Calculate average marks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            try:
                marks = float(input(f"Enter marks for {name}: "))
                students[name] = marks
                print(f"Student '{name}' added successfully!")
            except ValueError:
                print("Invalid input. Please enter numerical marks.")

        elif choice == "2":
            if not students:
                print("No student records found.")
            else:
                print("\n--- Student List ---")
                for name, marks in students.items():
                    print(f"Name: {name} | Marks: {marks:.2f}")

        elif choice == "3":
            if not students:
                print("No student records found.")
            else:
                name = input("Enter student name to search: ").strip()
                if name in students:
                    print(f"Found: {name} has {students[name]:.2f} marks.")
                else:
                    print(f"Student '{name}' not found.")

        elif choice == "4":
            if not students:
                print("No student records available to calculate average.")
            else:
                avg = sum(students.values()) / len(students)
                print(
                    f"Average marks of {len(students)} student(s): {avg:.2f}"
                )

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()