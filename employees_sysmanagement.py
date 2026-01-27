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
        Employee.all_employees.append(self)
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
        emp = Employee._find_by_emp_id(emp_id) 
        if emp:
            if data.get("name"): emp.name = data["name"]
            print(f"Employee {emp_id} updated successfully")
        else:
            print("Employee not found")
            
    #----delete employee from the set----         
    @classmethod
    def delete(cls, emp_id):
        emp = cls._find_by_emp_id(emp_id)
        if emp:
            cls.all_employees.remove(emp)
            cls.employees_ids.remove(emp.emp_id)
            print(f"Employee {emp_id} is deleted successfully")
    
    #delete Object by passing
    def delete_obj(self):
        Employee.delete(self.emp_id)
    
    @classmethod
    def list_employees(cls):
        list_all =cls.all_employees
        # want = input(" Do you wanna search or sort employees list: (search / sort):").lower()
        
        # if want == "search":
            
        wanna_search = input("Do you wanna search? (yes/No): ").lower()
            
        if wanna_search == "yes":
            term = input("Enter search term (emp_id or name): ").lower()
            list_all = list(filter(lambda emp: str(term) == str(emp.emp_id) or term.lower() in emp.name.lower(), list_all))
                
            print("\n--- Employee List ---")
            print("-" * 60)
            print(f"{'NO.':<15} {'ID':<15} {'Name':<20}")
            print("-" * 60)
            for e in list_all:
                print(f"{Employee.employees_ids:<15} {e.emp_id:<15} {e.name:<20}")
            
        sort = cls.all_employees   
        wanna_sort = input("Do you wanna search employees? (yes/No): ").lower()
        if wanna_sort == "yes":
            sort_by = input("How sort by (emp_id or name)? ").lower()
            if sort_by == "emp_id":
                    sort.sort(key=lambda emp: emp.emp_id)
            elif sort_by == "name":
                    sort.sort(key=lambda emp: emp.name.lower())
                    
        print("\n--- Employee List ---")
        print("-" * 90)
        print(f"{'NO.':<15} {'ID':<15} {'Name':<20}")
        print("-" * 90)
        
        for e in sort:
            print(f"{Employee.employees_ids:<15} {e.emp_id:<15} {e.name:<20}")
            
    
    #----find employee by emp_id----    
    @classmethod
    def _find_by_emp_id(cls, emp_id):
        return next(filter(lambda e:e.emp_id == emp_id,cls.all_employees  ), None)

    
    
    
    def __str__(self):
        return "Done"
    
    def __repr__(self):
        return f"Employee(id={self.emp_id}, name='{self.name}')"    

try:
    e1 = Employee.create({"emp_id":1, "name": "Rasha"})
    e2 = Employee.create({"emp_id":2, "name": "Amel"})
    e3 = Employee.create({"emp_id":3, "name": "Omer"})
    
    print (Employee.all_employees)
    Employee.update(1,{"name":"" })
    print (Employee.all_employees)
    Employee.list_employees()
    
    
    # e2 = Employee({"emp_id":1, "name": "Rasha"})
except ValueError as e:
    print(e)

