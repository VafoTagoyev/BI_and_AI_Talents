databaseName = "employees.txt"

user_menu_list = ["Add new employee record",
                  "View all employee records",
                  "Search for an employee by Employee ID",
                  "Update an employee's information",
                  "Delete an employee record",
                  "Exit"]


# user_menu_list = """
#     1. Add new employee record,
#     2. View all employee records,
#     3. Search for an employee by Employee ID,
#     Update an employee's information,
#     Delete an employee record,
#     Exit
# """

def greating():
    print()
    print("*" * 40)
    print("Welcome Customer Manager Software".center(40))
    print("*" * 40)
    print()


greating()


def max_employee_id():
    """
    Find max employee id from text file  when program starts
    """
    with open(file=databaseName, mode="r") as f:
        if f.read(1):
            f.seek(0)
            lastID = int(f.readlines()[-1].split(", ")[0])
            return lastID
        else:
            # initial value for employee id
            return 1000


def id_builder(start_id=None):
    """
    Generate unique IDs for employees
    """
    if start_id is None:
        current_id = max_employee_id()  # Get the maximum ID from the database
    else:
        current_id = start_id

    while True:
        current_id += 1
        yield current_id


def print_user_menu(user_menu_list):
    """
    Print menu
    """
    print("Select an item:")
    for index, element in enumerate(user_menu_list):
        print(f"{index + 1}: {element}")


employee_id = id_builder()


def add_employee(name, position, solary):
    """
    Add new employee
    """
    with open(file=databaseName, mode="a") as f:
        f.write(f"{next(employee_id)}, {name}, {position}, {solary}\n")


def view_employee():
    """
    Display all employee
    """
    with open(file=databaseName, mode="r") as f:
        for i in f:
            print(i, end='')


def search_employee():
    """
    Enter employee id for employee's information
    """
    id = input("Enter employee id: ")
    with open(file=databaseName, mode="r") as f:
        database = f.readlines()
    for row in database:
        if id in row.split(', ')[0]:
            print(row)
            break
    else:
        print(f"id:{int(id)} - Bunday foydalanuvchi mavjud emas!")


def delete_employee():
    """
    Delete employee by employee ID
    """
    id = input("Enter employee id: ")
    with open(file=databaseName, mode="r") as f:
        database = f.readlines()

    with open(file=databaseName, mode="w") as f:
        for rowdata in database:
            if id in rowdata.split(', ')[0]:
                continue
            else:
                f.write(rowdata)


def update_employee():
    """
    Update employee information by employee ID
    """
    id = input("Enter employee ID to update: ")

    with open(file=databaseName, mode="r") as f:
        database = f.readlines()

    for i, row in enumerate(database):
        if id in row.split(', ')[0]:
            print("Current information: ", row.strip())
            name = input("Enter new name (leave blank to keep current): ")
            position = input("Enter new position (leave blank to keep current): ")
            salary = input("Enter new salary (leave blank to keep current): ")

            name = name if name else row.split(', ')[1]
            position = position if position else row.split(', ')[2]
            salary = salary if salary else row.split(', ')[3]

            database[i] = f"{id}, {name}, {position}, {salary}\n"
            break
    else:
        print(f"Employee with ID {id} not found!")
        return

    with open(file=databaseName, mode="w") as f:
        f.writelines(database)
    print(f"Employee with ID {id} has been updated.")


def display_menu(option):
    """
    Display menu for user
    """
    match option:
        case 1:
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = input("Enter employee salary: ")
            add_employee(name, position, salary)
        case 2:
            view_employee()
        case 3:
            search_employee()
        case 4:
            update_employee()
        case 5:
            delete_employee()
        case 6:
            print("Exiting the system.")
            return False
        case _:
            print("Invalid option, please try again.")
            return True
    return True


def main():
    """
    Main function to run programm
    """
    greating()
    while True:
        print_user_menu(user_menu_list)
        try:
            option = int(input("Choose an option: "))
            if not display_menu(option):
                break
        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == '__main__':
    # start programm
    main()