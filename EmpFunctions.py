from datetime import datetime
# As DataBase
employees =[
        {"emp_id" : 1920201 , "name": "Ahmed Ali", "joining_date": "01/06/2012" ,"salary": 50000, "department" : "Back-end"},
        {"emp_id" : 1920202 , "name": "Asma Hankkkkki", "joining_date": "02/01/2012" , "salary": 50000, "department" : "Back-end"}
    ]
#[1] List Function
def list_employees(data=None):

    target = data if data is not None else employees
    print("-" * 90)
    print(f"{'ID':<15} {'Name':<20} {'Joining Date':<20} {'Department':<20} {'Salary':<15}")
    print("-" * 90)
    for emp in target:
        print(f"{emp['emp_id']:<15} {emp['name']:<20} {emp['joining_date']:<20} {emp['department']:<20} {emp['salary']:<15}\n")
        
#[2] Search
def search_employee():
    requesrt = input("Search Employee by or Name: ").strip()
    result = list(filter(lambda emp: requesrt.lower() in emp["name"].lower() or requesrt in str(emp["emp_id"]), employees))
    if result:
        list_employees(result)
    else:
        print(f"No results found for: '{requesrt}'")

#[3] Creat New Employee
def add_employ():
    # we can use this if we make programe automatic add ID
    # last_id = employees[-1:][0]["emp_id"]
    # ID = last_id +1
    
    new_emp = {"emp_id": check_id(), 
               "name": input("Enter Name: ").strip().title(),
               "joining_date": check_date(),
               "salary": check_salary(),
               "department": input("Enter Deprtment: ")
               }
    employees.append(new_emp)
    print("Good! New Employee is Added")

#[4] Update employee
def update_employ():
    try:
        emp_id = int(input("Enter ID of the Employee you wanna udate it:"))
        is_found = False
        for emp in employees:
            if emp["emp_id"] == emp_id:
                is_found = True
                emp["name"] = input(f"Update Name [{emp['name']}]: ").strip().title() or emp["name"]
                emp["joining_date"] = check_date(is_update = True) or emp["joining_date"]
                emp["salary"] = check_salary(is_update = True) or emp["salary"]
                emp["department"] = input(f"update Deprtmen [{emp['department']}]: ") or emp["department"]
            
        if not is_found:
            print(f"This Id is not Found..")
                
    except ValueError:
        print("Please enter a numeric ID.")

#[5] Delete employee
def remove_employ():
    emp_id = int(input("Enter Employee Id to delete: ").strip())
    global employees
    count = len(employees)
    employees = list(filter(lambda emp : emp["emp_id"] != emp_id, employees ))
    if len(employees) < count:
        print("Deleted successfully.")
    else:
        print("ID not found.")

#[6] check Salary
def check_salary(is_update=False):
    while True:
        sal = input("Enter Salary amount: ").strip()

        if not sal:
            if is_update:
                return None
            else:
                print("Salary is required for new employees!")
                continue
        try:
            salary = float(sal)
            if salary <= 0:
                print("The Salary must be positive number..")
                continue
            return salary
        
        except ValueError:
            print("Enter Jus Numbers..")

#[7] Check Date
def check_date(is_update=False):
    while True:
        date = input("Joining Date (DD/MM/YYYY): ")

        if not date and is_update:
            return None
        try:
            valid_date = datetime.strptime(date, "%d/%m/%Y")
            if valid_date > datetime.now():
                print("Error: This Date is in The Future!")
                continue
            return date
        except ValueError:
            if not date and not is_update:
                print("Date is required for new employees!")
            else:
                print("Follw This way Like: 24/1/2025")

#[8] Check Id
def check_id():
    while True:
        try:
            Id = int(input("Enter The ID: "))
            is_found = False 

            for emp in employees:
                if Id == int(emp["emp_id"]):
                    print("Error: This ID already exists, try again..")
                    is_found = True 
                    break               

            if not is_found:
                break 
        except ValueError:
            print("Invalid Value..Enter just Numbers")

#[9] Group
def group_by_dept():
    summary = {}
    for emp in employees:
        dept = emp['department']
        summary[dept] = summary.get(dept, 0) + emp['salary']
    
    print(f"\n{'Department':<20} | {'Total Salaries':<15}")
    print("-" * 40)
    for dept, total in summary.items():
        print(f"{dept:<20} | {total:<15}")

#[10] Sorting
def sort_data():
    return sorted(employees, key=lambda emp: datetime.strptime(emp['joining_date'], "%d/%m/%Y"))

#[11] Get 1st and 2nd Employee
def get_first_last_emp():
    sorted_list = sort_data()
    
    if not sorted_list:
        print("The list is empty!")
        return

    first = sorted_list[0]
    last = sorted_list[-1]
    
    print(f"The 1st Employee is {first['name']} (Joined: {first['joining_date']})")
    print(f"The Last Employee is {last['name']} (Joined: {last['joining_date']})")

    