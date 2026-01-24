import EmpFunctions

def main():
    while True:
            print("\n--- Employee System Management ---")
            print("\n--- DashaBoard ---\n")
            print("1. List All | 2. Add | 3. Update | 4. Delete | 5. Search | 6. Dept Totals | 7. Tenure Info | 8. Exit")
            c = input("Choice: ")
            if c == '1': EmpFunctions.list_employees()
            elif c == '2': EmpFunctions.add_employ()
            elif c == '3': EmpFunctions.update_employ()
            elif c == '4': EmpFunctions.remove_employ()
            elif c == '5': EmpFunctions.search_employee()
            elif c == '6': EmpFunctions.group_by_dept()
            elif c == '7': EmpFunctions.get_first_last_emp()
            elif c == '8': break
            else: print("Invalid choice.")

if __name__ == "__main__":
    main()

