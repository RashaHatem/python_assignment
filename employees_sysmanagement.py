class Employee:
    
    #----class Variable----
    employees_ids = set()
    id_counter = 1
    all_employees = []
    
    
    def __init__(self,data):
        emp_id = data.get("emp_id")
        if emp_id in Employee.employees_ids:
            raise ValueError (f"Error! This ID {emp_id} is already exists..")
        self.id= Employee.id_counter
        self.emp_id = emp_id
        self.name = data.get("name")
        
        Employee.employees_ids.add(self.emp_id)
        Employee.all_employees.append({"id": self.id, "emp_id": self.emp_id, "name": self.name})
        Employee.id_counter +=1
        
    
    #----create employee----    
    @classmethod
    def create(cls, data):
        return cls(data)
    
    #----save employee----
    def save(self):
        return f"Employee {self.name} is saved sucuccefly"
    
    #----update employee----
    @classmethod
    def update(cls , emp_id, data):
        emp = cls._find_by_emp_id(emp_id) 
        if emp:
            if data.get("name"): 
                emp["name"] = data["name"]
            
            print(f"Employee {emp_id} updated successfully")
        else:
            print("Employee not found")
            
    #----delete employee from the set----         
    @classmethod
    def delete(cls, emp_id):
        emp = cls._find_by_emp_id(emp_id)
        if emp:
            cls.all_employees.remove(emp)
            cls.employees_ids.remove(emp["emp_id"])
            
            print(f"Employee {emp_id} is deleted successfully")
        else:
            print("Employee not found")
    
    #delete Object by passing
    def delete_obj(self):
        Employee.delete(self.emp_id)
    
    @classmethod
    def search_employees(cls):
        list_all =cls.all_employees
   
        wanna_search = input("Do you wanna search? (yes/No): ").lower()
            
        if wanna_search == "yes":
            term = input("Enter search term (emp_id or name): ").lower()
            list_all = list(filter(lambda emp: str(term) == str(emp['emp_id']) or term.lower() in emp['name'].lower(), list_all))
            Employee.list_emploeey(list_all)
            
    @staticmethod
    def list_emploeey(data):
        print("\n--- Employee List ---")
        print("-" * 60)
        print(f"{'NO.':<10} {'ID':<15} {'Name':<20}")
        print("-" * 60)
        for e in data:
            print(f"{e['id']:<9} {e['emp_id']:<15} {e['name']:<20}") 
    
    @classmethod        
    def sort_employees(cls):
        sort = cls.all_employees   
        wanna_sort = input("Do you wanna sort employees? (yes/No): ").lower()
        if wanna_sort == "yes":
            sort_by = input("How sort by (emp_id or name)? ").lower()
            if sort_by == "emp_id":
                    sort.sort(key=lambda emp: emp['emp_id'])
            elif sort_by == "name":
                    sort.sort(key=lambda emp: emp['name'].lower())
                    
        Employee.list_emploeey(sort)
            
    #----find employee by emp_id----    
    @classmethod
    def _find_by_emp_id(cls, emp_id):
        return next(filter(lambda e:e['emp_id'] == emp_id,cls.all_employees  ), None)

    
    def __str__(self):
        return "Done"
    
    def __repr__(self):
        return f"Employee(id={self.emp_id}, name='{self.name}')"    

try:
    
    e1 = Employee.create({"emp_id":1920201, "name": "Rasha"})
    e2 = Employee.create({"emp_id":1920202, "name": "Amel"})
    e3 = Employee.create({"emp_id":1920203, "name": "Omer"})
    
    # e2 = Employee({"emp_id":1, "name": "Rasha"})
except ValueError as e:
    print(e)

def add_one():
    print("\n--- Add New Employee ---")
    while True:
        try:
            name = input("Enter Employee name (or type 'exit' to cancel): ").strip().title()
            if name.lower() == 'exit':
                break
            if not name:
                print("Error: Name cannot be empty!")
                continue

            emp_id = input("Enter Employee ID: ").strip()
            if emp_id.isdigit():
                emp_id = int(emp_id)
                
            if not emp_id:
                print("Error: ID is required!")
                continue

           
            data = {"name": name, "emp_id": emp_id}
            
            Employee(data)
            
            print(f"Employee {name} added successfully!")
            break 

        except ValueError as e:
        
            print(f"{e}")
def udate_one():
    try:
        emp_id = int(input("Enter Employee id to update it: ").strip())
        
        new_name =input("Enter new name: ").strip().title()
        
        data = {"name":new_name}
        
        Employee.update(emp_id, data)
        
    except ValueError:
        print(f"{emp_id} not digit, Ener numric id")
   
def del_one():
    try:
        emp_id = int(input("Enter Employee id to update it: ").strip())
        
        Employee.delete(emp_id)
        
    except ValueError:
        print(f"{emp_id} not digit, Ener numric id")         
            
def main():
    while True:
            print("\n--- Employee System Management ---")
            print("\n--- DashaBoard ---\n")
            print("1. List All | 2. Add | 3. Update | 4. Delete | 5. Search | 6. Sort | 7. Exit")
            c = input("Choice: ")
            if c == '1': Employee.list_emploeey(Employee.all_employees)
            elif c == '2': add_one() 
            elif c == '3': udate_one()
            elif c == '4': del_one()
            elif c == '5': Employee.search_employees()
            elif c == '6': Employee.sort_employees()
            elif c == '7': break
            else: print("Invalid choice.")

if __name__ == "__main__":
    main()

