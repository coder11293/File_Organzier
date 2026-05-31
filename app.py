import os

# Create a new file
def create_file(filename):
    try:
        with open(filename, 'x') as file:
            print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print(f"File '{filename}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")


# View all files in the current directory
def view_all_files():
    files = os.listdir()

    if not files:
        print("No files found in the current directory.")
    else:
        print("\nFiles in the current directory:")
        for file in files:
            print(file)


# Delete a file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Read a file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        print(f"\nContent of '{filename}':")
        print(content)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Edit a file
def edit_file(filename):
    try:
        new_content = input("Enter new content for the file: ")

        with open(filename, 'w') as file:
            file.write(new_content + "\n")

        print(f"File '{filename}' updated successfully.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main menu
def main():
    while True:
        print("\n===== FILE ORGANIZER MENU =====")
        print("1. Create a new file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Read a file")
        print("5. Edit a file")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter the file name to create: ")
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input("Enter the file name to delete: ")
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter the file name to read: ")
            read_file(filename)

        elif choice == '5':
            filename = input("Enter the file name to edit: ")
            edit_file(filename)

        elif choice == '6':
            print("Exiting File Organizer. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()