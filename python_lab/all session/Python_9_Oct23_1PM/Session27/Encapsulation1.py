'''
Access Specifier:To achieve Encapsulation we have to use access specifier to provide security.

Public Member:Those members which are generated without any additional naming convention.

eg: data(), count
===========
Private Member:Those members which are generated with __state of name.

eg:__data(), __count

'''

class _Employee:
    def setdetails(self,eid,ename):
        self.eid=eid
        self.ename=ename
    def getdetails(self):
        print("Employee Id:",self.eid)
        print("Employee Name:",self.ename)
#-- 

emp = _Employee()
emp.setdetails(121,"Rahul Sharma") 
print("======== Before Changes ============")
emp.getdetails()
emp.eid=120
print("======== After Change ============")
emp.getdetails()       
