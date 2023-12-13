'''
Static :
Single Memory Allocation.
All objects of a class shared memory of static variable. 
Accessing variable using className then that variable is said to be static variable.
It gets memory at compile time.

'''
class Example:

    count=0
    #static 
    counter=0

    def increment(self):
        # self.count+=1
        # print("Count is:",self.count)
        Example.counter+=1
        print("Example is:",Example.counter)

    #Convert a function to be a static method.
    @staticmethod
    def msg():
        print("Heloo")    


#---- 
Example.msg()
Example().increment()
Example().increment()
Example().increment()
Example().increment()
Example().increment()
