class Employee:
    details={}
    sal={}
    def __init__(self,empid, empname, salary):
        self.empname = empname
        self.empid = empid
        self.salary = salary
        self.managerid = None
        self.manangername=None
        self.managersal=None
        Employee.details[empid]=empname
        Employee.sal[empid]=salary
    def assignmanager(self,managerid):
        if managerid in Employee.details:
            if int(Employee.sal.get(managerid)) < int(self.salary):
                self.managerid=managerid
                f'manger is assigned to {self.managerid}'
            else:
                print("employee salary is lower than manager")
        else:
            print("not a valid id ")
    def description(self):
        return (f'{self.empname} is employee id  {self.empid} of salary {self.salary} assigned to manager id {self.managerid} ')

Emp1=Employee(1,"aakash",10000)
Emp2=Employee(2,"jay",20000)
Emp3=Employee(3,"janvi",30000)
Emp4=Employee(4,"shubham",40000)
Emp1.assignmanager(2)
Emp1.description()class Employee:
    details={}
    sal={}
    def __init__(self,empid, empname, salary):
        self.empname = empname
        self.empid = empid
        self.salary = salary
        self.managerid = None
        self.manangername=None
        self.managersal=None
        Employee.details[empid]=empname
        Employee.sal[empid]=salary
    def assignmanager(self,managerid):
        if managerid in Employee.details:
            if int(Employee.sal.get(managerid)) < int(self.salary):
                self.managerid=managerid
                print("manager is assigned")
            else:
                print("employee salary is lower than manager")
        else:
            print("not a valid id ")
    def description(self):
        return (f'{self.empname} is employee id  {self.empid} of salary {self.salary} assigned to manager id {self.managerid} ')

Emp1=Employee(1,"aakash",10000)
Emp2=Employee(2,"jay",20000)
Emp3=Employee(3,"janvi",30000)
Emp4=Employee(4,"shubham",40000)
Emp1.assignmanager(4)
Emp1.description()