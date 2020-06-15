import time
starttime=time.time()
class Employee:
    details=dict()
    sal=dict()

    def __init__(self, empid, empname, salary):
        self.empid=empid
        self.empname=empname
        self.salary=salary
        self.managerid=None
        Employee.details[empid]=empname
        Employee.sal[empid]=salary

    def assignmgr(self, managerid):
        if managerid in Employee.details:
            if int(Employee.sal.get(managerid)) > int (self.salary):
                self.managerid=managerid

    def showdetails(self):
        print(f'employee name {self.empname} with employee id {self.empid} has salary {self.salary} under manager of id {self.managerid}')


emp1= Employee(101,'js',30000)
emp2= Employee(102,'jj',27000)
emp3= Employee(103,'as',40000)
emp14= Employee(104,'ss',25000)

emp2.assignmgr(101)
emp2.showdetails()

endtime=time.time()
executiontime=endtime-starttime

print(executiontime)





