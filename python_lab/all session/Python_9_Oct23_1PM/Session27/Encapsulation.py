'''
Encapsulation:It is an object oriented feature which signifies wrapping up of data into a single unit.It is used for security purpose.
'''

class Employee:
    def setdetails(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def getdetails(self):
        print("Employee Id:",self.eid)
        print("Employee Name:",self.ename)
#-- 

emp = Employee()
emp.setdetails(121,"Rahul Sharma") 
print("======== Before Changes ============")
emp.getdetails()
emp.eid=120
print("======== After Change ============")
emp.getdetails()       
