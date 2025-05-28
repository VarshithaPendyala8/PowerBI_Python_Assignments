"""      
Q). Create a class with name of dept which has id, name, loc, HOD through 
the constructor initialize the department  attributes
create  a method to display the dept. info, display total dept in your organization.

-Get the input from the user no.of dept, create list/dict to store the no.of dept
-use for loop to get the dept information
-for every dept info u get, add that into list/dict,  
-display all dept info in the list/dict
-search dept by dept_id, if it is there show details else  it is not available
-add a fun. to search for dept by dept_name 
"""
class Department:
    dept_count = 0
    def __init__(self, id, name, loc, hod): 
        self.dept_id = id
        self.dept_name = name
        self.dept_loc = loc
        self.dept_hod = hod
        Department.dept_count += 1

    def display_dept_info(self):
        print("\nDepartments Information:")
        print("-------------------")
        print(f"Department ID: {self.dept_id}")
        print(f"Department Name: {self.dept_name}")
        print(f"Department Location: {self.dept_loc}")
        print(f"Department HOD: {self.dept_hod}")

    @classmethod 
    def get_total_departments(cls): 
        print(f"Total Departments in organization: {cls.dept_count}")

# dept1 = Department("004", "ECE", "Opal Block", "Nagesh")
# dept2 = Department("001", "CSE", "Diamond Block", "David")

# print(f"Total_Departments: {Department.get_total_departments()}")

dept_list = []
n = int(input("Enter no.of departments:"))
for i in range(n):
    print(f"\nEnter details of department {i+1}:")
    dept_id = input("Enter department ID: ")
    dept_name = input("Enter department name: ")
    dept_loc = input("Enter department location: ")
    dept_hod = input("Enter department HOD: ")

    details = Department(dept_id, dept_name, dept_loc, dept_hod)
    dept_list.append(details)


for d in dept_list:
    d.display_dept_info()

Department.get_total_departments()

# Searching by Department ID
id = input("\nEnter Department ID: ")
found = False
for d in dept_list:
    if d.dept_id == id:
        print("\nDepartment Found:")
        d.display_dept_info()
        found = True
        break
if not found:
    print("Department ID is not available.")

# Searching by Department Name
name = input("\nEnter Department Name: ")
found = False
for d in dept_list:
    if d.dept_name.lower() == name.lower():
        print("\nDepartment Found:")
        d.display_info()
        found = True
if not found:
    print("Department name is not available.")





    