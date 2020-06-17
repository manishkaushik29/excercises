import time
starttime=time.time()
class Employee:
    Store=dict()
    storesal=dict()
    def __init__(self,empid, empname, salary ):
        self.empid=empid
        self.empname=empname
        self.salary=salary
        self.managerid=None
        Employee.Store[empid]=empname
        Employee.storesal[empid]=salary


    def AssignManager(self,managerid):
        if managerid in Employee.Store :
            if int(Employee.storesal.get(managerid)) > int(self.salary):
                self.managerid = managerid




    def show(self):
        print(self.empid,self.empname,self.salary,self.managerid,Employee.Store.get(self.managerid))




emp1 = Employee(1,'ak', 10000)
emp2 = Employee(2,'as', 20000)
emp3 = Employee(3,'ss', 30000)

emp1.AssignManager(3)
emp1.show()

print(time.time()-starttime)